from typing import Optional
import openai
from .image import encode_image_to_base64

def analyze_image(
    image,
    endpoint_url: str,
    api_key: str,
    selected_model: str,
    prompt: str,
    system_prompt: Optional[str] = None,
    temperature: float = 1.0
):
    """Analyze image using LiteLLM with custom prompts"""
    if not endpoint_url or not api_key:
        return "Please configure both the endpoint URL and API key"
    
    if not selected_model:
        return "Please select a model"
    
    print(f"Analyzing image with model: {selected_model}")
    
    try:
        client = openai.OpenAI(
            api_key=api_key,
            base_url=endpoint_url 
        )

        # Convert image to base64
        base64_image = encode_image_to_base64(image)
        
        # Prepare messages
        messages = []
        
        # Add system prompt if provided
        if system_prompt:
            messages.append({
                "role": "system",
                "content": system_prompt
            })
        
        # Add user message with image
        messages.append({
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": base64_image}
            ]
        })
        
        # Call LiteLLM with custom endpoint
        response = client.chat.completions.create(
            model=selected_model,
            messages=messages,
            temperature=temperature
        )
        
        return str(response.choices[0].message.content)
            
    except Exception as e:
        return f"Error analyzing image: {str(e)}"