import base64
from io import BytesIO
from PIL import Image

def encode_image_to_base64(image: Image.Image) -> str:
    """Convert image to base64 string"""
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return f"data:image/png;base64,{img_str}"