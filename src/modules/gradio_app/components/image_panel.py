import gradio as gr
from typing import Tuple

def create_image_panel() -> Tuple[gr.Image, gr.Button, gr.Textbox]:
    """Create image upload and analysis panel"""
    with gr.Row():
        with gr.Column():
            image_input = gr.Image(
                label="Upload Image",
                type="pil"
            )
            analyze_button = gr.Button("Analyze Image")
            
        with gr.Column():
            output = gr.Textbox(
                label="Analysis Result",
                lines=10
            )

    return image_input, analyze_button, output