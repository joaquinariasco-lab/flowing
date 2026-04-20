from flowing.engine import FlowEngine

if __name__ == "__main__":
    print("\n=== FLOWING DEMO ===\n")

    schema_path = input("Path to schema JSON: ")
    prompt = input("Prompt for AI: ")

    engine = FlowEngine(max_attempts=5)

    result = engine.run(prompt=prompt, schema_path=schema_path)

    print("\n=== FINAL OUTPUT ===\n")
    print(result)
