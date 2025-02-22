"""Components for the Gradio application UI"""

from .config_panel import create_config_panel
from .prompt_panel import create_prompt_panel
from .image_panel import create_image_panel

__all__ = ['create_config_panel', 'create_prompt_panel', 'create_image_panel']