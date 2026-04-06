from fastapi import FastAPI
from app.routes import text, image, audio

app = FastAPI(title="Multimodal AI Data Copilot")

@app.get("/")
def root():
    return {"message": "API is running 🚀"}


app.include_router(text.router, prefix="/api")
app.include_router(image.router, prefix="/api")
app.include_router(audio.router, prefix="/api")
