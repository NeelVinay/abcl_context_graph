"""Entry point for the speech-to-text stage (mp3 recordings -> plain-text transcripts).

  python run_transcribe.py                 # up to 100 recordings from config.AUDIO_SRC
  python run_transcribe.py --limit 5       # quick batch
  python run_transcribe.py FILE [FILE...]  # specific recordings (validation)

Flags: --src DIR  --limit N  --model SIZE  --diar-device {cpu,mps}  --overwrite
Output: plain transcripts (Agent:/Customer:, one turn per line) in data/audio_transcripts/.
"""
from src.transcribe import main

if __name__ == "__main__":
    main()
