"""Clean GPU/CPU speed benchmark (run with NO other jobs competing for unified memory).
Times: (1) MLX Whisper large-v3 on GPU, (2) pyannote diarization on CPU vs MPS."""
import sys
import time
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import torch  # noqa: E402
_orig = torch.load
torch.load = lambda *a, **k: _orig(*a, **{**k, "weights_only": False})

F = str(Path.home() / "Downloads" / "leads_mp3_data" / "LCS-RDCGZZ1E" / "LCS-RDCGZZ1E.mp3")
DUR = 105.0


def bench_mlx():
    import mlx_whisper
    repo = "mlx-community/whisper-large-v3-mlx"
    mlx_whisper.transcribe(F, path_or_hf_repo=repo, language="hi")  # warmup
    t = time.time()
    mlx_whisper.transcribe(F, path_or_hf_repo=repo, language="hi")
    el = time.time() - t
    print(f"[MLX large-v3 GPU]   {el:.1f}s  = {DUR/el:.1f}x realtime   (CPU CTranslate2 was ~44s/2.4x)", flush=True)


def bench_diar(device):
    import whisperx
    from whisperx.diarize import DiarizationPipeline
    audio = whisperx.load_audio(F)
    try:
        dia = DiarizationPipeline(device=device)
        t = time.time()
        df = dia(audio, min_speakers=1, max_speakers=2)
        el = time.time() - t
        print(f"[pyannote diar {device:>3}]  {el:.1f}s  = {DUR/el:.1f}x realtime   "
              f"({len(df)} segs, speakers={sorted(df['speaker'].unique())})", flush=True)
    except Exception as e:
        print(f"[pyannote diar {device:>3}]  FAILED: {type(e).__name__}: {str(e)[:160]}", flush=True)


print("=" * 70, flush=True)
bench_mlx()
bench_diar("cpu")
bench_diar("mps")
print("=" * 70, flush=True)
