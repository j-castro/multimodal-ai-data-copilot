
from fastapi import APIRouter, UploadFile
from app.services.openai_client import get_client
from app.core.validators import validate_file_size
from app.core.config import settings
import io

router = APIRouter()

@router.post("/audio/transcribe")
async def transcribe_audio(file: UploadFile):
    client = get_client()
    validate_file_size(file, settings.MAX_AUDIO_SIZE_MB)

    contents = await file.read()

    audio_file = io.BytesIO(contents)
    audio_file.name = file.filename  # important!

    transcription = client.audio.transcriptions.create(
        model="gpt-4o-mini-transcribe",
        file=audio_file
    )

    return {"transcription": transcription.text}