# llm_client.py
# Handles Anthropic API communication

import os
from dotenv import load_dotenv
from openai import OpenAI

from app.prompt_utils import build_messages

# Load API key
load_dotenv()

API_KEY = os.getenv("ANTHROPIC_API_KEY")

if not API_KEY:
    raise ValueError("ANTHROPIC_API_KEY not found in .env file")

# Claude config
MODEL_NAME = "claude-sonnet-4-5-20250929"
BASE_URL = "https://api.anthropic.com/v1/"

# Create client
client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)


def generate_tests(code: str, module_name: str) -> str:
    """
    Send code to Claude and get test code
    """

    messages = build_messages(code, module_name)

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        reasoning_effort="high"
    )

    reply = response.choices[0].message.content

    return reply
