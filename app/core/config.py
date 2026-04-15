import os

class Settings:
    MAX_TEXT_LENGTH = int(os.getenv("MAX_TEXT_LENGTH", 5000))  # chars
    MAX_IMAGE_SIZE_MB = int(os.getenv("MAX_IMAGE_SIZE_MB", 5))  # MB
    MAX_AUDIO_SIZE_MB = int(os.getenv("MAX_AUDIO_SIZE_MB", 1))  # MB

settings = Settings()