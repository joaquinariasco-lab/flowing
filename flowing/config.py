import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    PROVIDER = os.getenv("FLOWING_PROVIDER", None)
    API_KEY = os.getenv("FLOWING_API_KEY", None)
    MODEL = os.getenv("FLOWING_MODEL", None)
