import json

def build_prompt(user_prompt: str, schema: dict) -> str:
    return f"""
You must follow this schema strictly:

SCHEMA:
{json.dumps(schema, indent=2)}

USER TASK:
{user_prompt}

Return ONLY valid JSON matching the schema. No explanation.
"""
