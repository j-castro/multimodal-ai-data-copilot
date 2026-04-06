from fastapi import APIRouter
from app.services.openai_client import get_client
from app.services.token_utils import estimate_tokens

router = APIRouter()


@router.post("/text")
async def process_text(prompt: str):
    client = get_client()

    input_tokens = estimate_tokens(prompt)

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )

    output_text = response.output_text

    output_tokens = estimate_tokens(output_text)

    return {
        "response": output_text,
        "input_tokens_estimated": input_tokens,
        "output_tokens_estimated": output_tokens
    }