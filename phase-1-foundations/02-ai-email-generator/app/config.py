import os
from dotenv import load_dotenv

# Load Environment Variables from .env file
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MODEL_NAME = "gpt-4.1-mini"
