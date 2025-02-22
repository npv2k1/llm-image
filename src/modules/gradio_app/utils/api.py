from typing import List
import requests

def get_available_models(endpoint_url: str, api_key: str) -> List[str]:
    """Fetch available models from LiteLLM endpoint"""
    try:
        response = requests.get(
            f"{endpoint_url.rstrip('/')}/models",
            headers={"Authorization": f"Bearer {api_key}"}
        )
        if response.status_code == 200:
            models = response.json()
            return [model["id"] for model in models["data"]]
        return []
    except Exception as e:
        print(f"Error fetching models: {e}")
        return []

def update_model_list(endpoint_url: str, api_key: str) -> List[str]:
    """Update the model list when endpoint or API key changes"""
    if not endpoint_url or not api_key:
        return []
    return get_available_models(endpoint_url, api_key)