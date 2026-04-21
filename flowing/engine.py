from .providers.factory import get_provider
from .schema import load_schema
from .validator import SchemaValidator
from .prompts import build_prompt
from .utils import safe_json_load


class FlowEngine:
    def __init__(self, max_attempts=3):
        self.llm = get_provider()
        self.validator = SchemaValidator()
        self.max_attempts = max_attempts

    def run(self, prompt: str, schema_path: str):
        schema = load_schema(schema_path)
        formatted = build_prompt(prompt, schema)

        for i in range(self.max_attempts):
            print(f"Attempt {i+1}/{self.max_attempts}")

            response = self.llm.generate(formatted)
            parsed = safe_json_load(response)

            if parsed and self.validator.validate(schema, parsed):
                return parsed

        raise Exception("Failed to generate valid output")
