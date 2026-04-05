from openai import OpenAI
from dotenv import load_dotenv
import os
import tiktoken

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print(f'API Key: {api_key}')

client = OpenAI()

enc = tiktoken.encoding_for_model("gpt-4o-mini")
tokens = len(enc.encode("Hello"))

print(f'Tokens used: {tokens}')

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=20
)

print(response.choices[0].message.content)


