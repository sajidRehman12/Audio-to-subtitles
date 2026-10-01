# Audio Translation API

A minimal FastAPI project scaffold for an audio transcription and translation service.

## Features

- FastAPI app with health and upload endpoints
- Upload an audio file and receive a transcription + translation placeholder response
- Ready for integration with Whisper, Deepgram, or another speech-to-text provider

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# or .venv\Scripts\activate  # Windows PowerShell
pip install -r requirements.txt
```

## Run locally

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Then open:

- http://localhost:8000/
- http://localhost:8000/docs

## Example upload

```bash
curl -X POST "http://localhost:8000/translate?target_language=es" \
  -F "file=@sample.wav"
```

## Project structure

```text
app/
  __init__.py
  main.py
  schemas.py
  services/
    __init__.py
    translation_service.py
requirements.txt
README.md
```
