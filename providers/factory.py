import requests
from ..config import Config
from .openai import OpenAIProvider
from .ollama import OllamaProvider


def is_ollama_running():
    try:
        r = requests.get("http://localhost:11434")
        return r.status_code == 200
    except:
        return False


def get_provider():
    # 1. If dev explicitly set provider → use it
    if Config.PROVIDER:
        if Config.PROVIDER == "openai":
            return OpenAIProvider()
        elif Config.PROVIDER == "ollama":
            return OllamaProvider()
        else:
            raise ValueError("Unknown provider")

    # 2. Auto-detect (default behavior)
    if is_ollama_running():
        print("Using Ollama (auto-detected)")
        return OllamaProvider()

    # 3. Fallback to OpenAI if API key exists
    if Config.API_KEY:
        print("Using OpenAI (API key detected)")
        return OpenAIProvider()

    # 4. Nothing available → fail clearly
    raise Exception(
        "No provider available. Start Ollama or set FLOWING_API_KEY."
    )
