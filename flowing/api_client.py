import requests
from .config import Config

class APIClient:
    def send_prompt(self, prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {Config.API_KEY}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": Config.MODEL,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(Config.API_URL, json=payload, headers=headers)

        if response.status_code != 200:
            raise Exception(f"API Error: {response.text}")

        data = response.json()

        return data["choices"][0]["message"]["content"]
