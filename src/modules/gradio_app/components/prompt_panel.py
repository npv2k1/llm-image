import gradio as gr
from typing import Tuple

def create_prompt_panel() -> Tuple[gr.Textbox, gr.Textbox, gr.Slider]:
    """Create custom prompt panel for image analysis"""
    with gr.Column():
        prompt_input = gr.Textbox(
            label="Custom Prompt",
            placeholder="Enter your prompt for image analysis...",
            lines=3,
            value="Please analyze this image in detail."
        )
        system_prompt = gr.Textbox(
            label="System Prompt (Optional)",
            placeholder="Enter a system prompt to guide the model...",
            lines=2,
            visible=False  # Hidden by default
        )
        with gr.Row():
            advanced_checkbox = gr.Checkbox(
                label="Show Advanced Options",
                value=False
            )
            temperature = gr.Slider(
                minimum=0.0,
                maximum=2.0,
                value=1.0,
                step=0.1,
                label="Temperature",
                visible=False
            )

        def toggle_advanced(show_advanced):
            return {
                system_prompt: gr.update(visible=show_advanced),
                temperature: gr.update(visible=show_advanced)
            }

        advanced_checkbox.change(
            fn=toggle_advanced,
            inputs=[advanced_checkbox],
            outputs=[system_prompt, temperature]
        )

    return prompt_input, system_prompt, temperature