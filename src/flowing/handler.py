import uuid
from typing import Dict, Any

def normalize_api_call(api_request: Dict[str, Any]) -> Dict[str, Any]:
    """
    Normalize developer API call and add metadata.
    
    Parameters:
        api_request (dict): The raw developer API request.
        
    Returns:
        dict: Normalized request with metadata.
    """
    # Step 1: Extract raw fields with defaults
    user_input = api_request.get("input", "")
    user_id = api_request.get("user_id", "anonymous")
    model = api_request.get("model", "gpt-5-mini")
    flags = api_request.get("flags", [])

    # Step 2: Normalize structure
    normalized_data = {
        "text": str(user_input),
        "user_id": str(user_id),
        "options": {
            "model": model,
            "flags": flags
        }
    }

    # Step 3: Add metadata
    normalized_data["context"] = {
        "project": api_request.get("project", "default_project"),
        "session_id": api_request.get("session_id", str(uuid.uuid4()))
    }
    normalized_data["model"] = model
    normalized_data["hints"] = flags

    # Step 4: Return fully prepared request
    return normalized_data


# Example usage
if __name__ == "__main__":
    # Simulate a developer API call
    dev_request = {
        "input": "Summarize this text",
        "user_id": 42,
        "flags": ["debug"],
        "project": "ai_text_summarizer"
    }

    prepared_request = normalize_api_call(dev_request)
    print(prepared_request)
