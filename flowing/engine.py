from .api_client import APIClient
from .schema import load_schema
from .validator import SchemaValidator
from .prompts import build_prompt
from .utils import safe_json_load


class FlowEngine:
    def __init__(self, max_attempts: int = 3):
        self.client = APIClient()
        self.validator = SchemaValidator()
        self.max_attempts = max_attempts

    def run(self, prompt: str, schema_path: str):
        schema = load_schema(schema_path)

        formatted_prompt = build_prompt(prompt, schema)

        for attempt in range(self.max_attempts):
            print(f"\nAttempt {attempt + 1}/{self.max_attempts}")

            response = self.client.send_prompt(formatted_prompt)
            parsed = safe_json_load(response)

            if parsed is None:
                print("Invalid JSON, retrying...")
                continue

            if self.validator.validate(schema, parsed):
                print("Valid response received.")
                return parsed

            print("Schema mismatch, retrying...")

        raise Exception("Failed to generate valid response after max attempts")
