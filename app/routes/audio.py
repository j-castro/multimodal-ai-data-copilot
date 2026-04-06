# from fastapi import APIRouter, UploadFile
# from app.services.openai_client import get_client

# router = APIRouter()

# @router.post("/audio/transcribe")
# async def transcribe_audio(file: UploadFile):
#     client = get_client()

#     audio_bytes = await file.read()

#     transcription = client.audio.transcriptions.create(
#         model="gpt-4o-mini-transcribe",
#         file=audio_bytes
#     )

#     return {"transcription": transcription.text}


from fastapi import APIRouter, UploadFile
from app.services.openai_client import get_client
import io

router = APIRouter()

@router.post("/audio/transcribe")
async def transcribe_audio(file: UploadFile):
    client = get_client()

    contents = await file.read()

    audio_file = io.BytesIO(contents)
    audio_file.name = file.filename  # important!

    transcription = client.audio.transcriptions.create(
        model="gpt-4o-mini-transcribe",
        file=audio_file
    )

    return {"transcription": transcription.text}