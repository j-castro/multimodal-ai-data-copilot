
from fastapi import APIRouter, UploadFile
import base64
from app.services.openai_client import get_client

router = APIRouter()


@router.post("/image")
async def analyze_image(file: UploadFile):
    client = get_client()

    contents = await file.read()
    base64_image = base64.b64encode(contents).decode("utf-8")

    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": "Describe this image"},
                    {
                        "type": "input_image",
                        "image_url" : f"data:{file.content_type};base64,{base64_image}"
                    }
                ]
            }
        ]
    )

    return {"result": response.output_text}