import os

class Config:
    # Replace with your actual API endpoint
    API_URL = os.getenv("FLOWING_API_URL", "https://api.openai.com/v1/chat/completions")
    API_KEY = os.getenv("FLOWING_API_KEY", "your-api-key")

    MODEL = os.getenv("FLOWING_MODEL", "gpt-4o-mini")
