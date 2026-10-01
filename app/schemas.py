from pydantic import BaseModel, Field


class TranslationRequest(BaseModel):
    filename: str = Field(..., description="Audio filename")
    target_language: str = Field(default="en", description="Language to translate to")


class TranslationResponse(BaseModel):
    filename: str
    source_language: str = "auto"
    target_language: str
    transcription: str
    translation: str
