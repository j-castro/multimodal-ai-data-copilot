from fastapi import HTTPException, UploadFile
from app.core.config import settings

def validate_text_length(text: str):
    if len(text) > settings.MAX_TEXT_LENGTH:
        raise HTTPException(
            status_code=400,
            detail=f"Text exceeds max length of {settings.MAX_TEXT_LENGTH} characters"
        )

def validate_file_size(file: UploadFile, max_size_mb: int):
    file.file.seek(0, 2)  # move to end
    size = file.file.tell()
    file.file.seek(0)

    size_mb = size / (1024 * 1024)
    if size_mb > max_size_mb:
        raise HTTPException(
            status_code=400,
            detail=f"File exceeds max size of {max_size_mb} MB"
        )