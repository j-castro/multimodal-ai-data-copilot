from fastapi import APIRouter
from app.services.openai_client import get_client
from app.services.token_utils import estimate_tokens
from app.core.validators import validate_text_length

router = APIRouter()


@router.post("/text")
async def process_text(prompt: str):

    client = get_client()
    validate_text_length(prompt) # validate text length before processing

    #input_tokens = estimate_tokens(prompt)

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )

    #output_text = response.output_text
    #output_tokens = estimate_tokens(output_text)

    token_dict = {
        'prompt_tokens':response.usage.input_tokens,
        'completion_tokens':response.usage.output_tokens,
        'total_tokens':response.usage.total_tokens,
    }

    return {
        "response": response.output_text,
        "tokens": token_dict
    }