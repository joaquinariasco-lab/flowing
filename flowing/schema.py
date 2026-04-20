import json

def load_schema(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)
