import os
from openai import OpenAI

from settings import TOKEN
token = TOKEN
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "What is the capital of France?",
        },
        {
            "role": "assistant",
            "content": "The capital of France is Paris.",
        },
        {
            "role": "user",
            "content": "What about Spain?",
        }
    ],
    model=model_name,
)

print(response.choices[0].message.content)