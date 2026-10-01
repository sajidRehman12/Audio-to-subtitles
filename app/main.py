from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import TranslationRequest, TranslationResponse
from app.services.translation_service import TranslationService

app = FastAPI(
    title="Audio Translation API",
    version="0.1.0",
    description="API for transcribing and translating audio files.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

service = TranslationService()


@app.get("/")
def read_root():
    return {
        "message": "Audio Translation API is running",
        "docs": "/docs",
        "health": "/health",
        "translate": "/translate",
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/translate", response_model=TranslationResponse)
async def translate_audio(
    file: UploadFile = File(...),
    target_language: str = "en",
):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file was uploaded.")

    transcription = await service.transcribe_audio(file)
    translation = await service.translate_text(transcription, target_language)

    return TranslationResponse(
        filename=file.filename,
        source_language="auto",
        target_language=target_language,
        transcription=transcription,
        translation=translation,
    )


@app.post("/demo-translate")
def demo_translate(payload: TranslationRequest):
    return {
        "message": "Demo translation request received.",
        "filename": payload.filename,
        "target_language": payload.target_language,
        "transcription": f"Demo transcription for {payload.filename}",
        "translation": f"Demo translated text in {payload.target_language}",
    }
