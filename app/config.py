import os
from dotenv import load_dotenv

load_dotenv()

def get_openrouter_api_key():
    key = os.getenv("OPENROUTER_API_KEY")
    if not key:
        raise ValueError("OPENROUTER_API_KEY not set in .env")
    return key
