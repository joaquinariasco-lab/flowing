import json

def safe_json_load(text: str):
    try:
        return json.loads(text)
    except Exception:
        return None
