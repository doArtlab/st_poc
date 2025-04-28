from openai import OpenAI
from config import Config

client = OpenAI(api_key=Config.openai_api_key)

def generate_text(instruction: str, input: str, model: str = "gpt-4o-mini"):
    response = client.responses.create(
        model=model,
        instructions=instruction,
        input=input
    )
    return response.output_text