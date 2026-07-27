"""Dev-only: run the expensive models ONCE on a couple of calls and pickle the
intermediate artifacts (whisper segments, aligned words, diarization df), so the
turn-assembly logic can be iterated in milliseconds without re-running models."""
import pickle
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src import transcribe  # noqa: E402  (applies torch.load patch on import)

B = Path.home() / "Downloads" / "leads_mp3_data"
FILES = [
    B / "LCS-RDCGZZ1E" / "LCS-RDCGZZ1E.mp3",   # short, clean back-and-forth
    B / "LCS-Y48ZNWY7" / "LCS-Y48ZNWY7.mp3",   # longer, dense turn-taking
]
OUT = Path("/tmp/stt_debug.pkl")

models = transcribe.load_models()
whisperx = models["whisperx"]
data = {}
for f in FILES:
    print(f"... {f.name}")
    audio = whisperx.load_audio(str(f))
    result = models["asr"].transcribe(audio, batch_size=4)
    segments = [s for s in result["segments"]
                if not transcribe._is_hallucination((s.get("text") or "").strip())]
    diar_df = models["diar"](audio, min_speakers=1, max_speakers=2)
    aligned = whisperx.align(segments, models["align_model"], models["align_meta"],
                             audio, "cpu", return_char_alignments=False)
    data[f.stem] = {"segments": segments, "aligned": aligned,
                    "diar": diar_df.to_dict("records")}
    print(f"    diar segments: {len(diar_df)}  speakers: {sorted(diar_df['speaker'].unique())}")

OUT.write_bytes(pickle.dumps(data))
print(f"wrote {OUT}")
