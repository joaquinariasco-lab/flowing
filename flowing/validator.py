from jsonschema import validate, ValidationError

class SchemaValidator:
    def validate(self, schema: dict, data: dict) -> bool:
        try:
            validate(instance=data, schema=schema)
            return True
        except ValidationError:
            return False
