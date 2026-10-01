from fastapi import UploadFile


class TranslationService:
    async def transcribe_audio(self, file: UploadFile) -> str:
        """Replace this with a real ASR engine such as Whisper or Deepgram."""
        filename = file.filename or "audio"
        return f"Demo transcription for '{filename}'. Connect a speech-to-text provider here."

    async def translate_text(self, text: str, target_language: str) -> str:
        """Replace this with a real translation provider or model."""
        return f"[{target_language}] {text}"
