# import tiktoken

# def estimate_tokens(text: str, model: str = "gpt-4o-mini"):
#     encoding = tiktoken.encoding_for_model(model)
#     tokens = encoding.encode(text)
#     return len(tokens)

import tiktoken

def estimate_tokens(text: str, model: str = "gpt-4o-mini"):
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        # fallback if model not recognized
        encoding = tiktoken.get_encoding("cl100k_base")

    tokens = encoding.encode(text)
    return len(tokens)