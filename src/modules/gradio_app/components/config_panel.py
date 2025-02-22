import gradio as gr
from typing import Tuple

from src.modules.gradio_app.utils.api import update_model_list

def create_config_panel() -> Tuple[gr.Textbox, gr.Textbox, gr.Dropdown]:
    """Create configuration panel with endpoint, API key and model selection"""
    with gr.Column():
        endpoint_url = gr.Textbox(
            label="LiteLLM Endpoint URL",
            placeholder="Enter your LiteLLM endpoint URL",
        )
        api_key = gr.Textbox(
            label="API Key",
            placeholder="Enter your API key",
            type="password"
        )
        refresh_models = gr.Button("Refresh Models")
        model_dropdown = gr.Dropdown(
            label="Select Model",
            choices=[],
            interactive=True
        )

        # Update model list when endpoint or API key changes
        def update_models(endpoint_url, api_key):
            models = update_model_list(endpoint_url, api_key)
            return gr.Dropdown(choices=models)
        
        refresh_models.click(
            fn=update_models,
            inputs=[endpoint_url, api_key],
            outputs=model_dropdown
        )
        
        # Update models automatically when endpoint or API key changes
        endpoint_url.change(
            fn=update_models,
            inputs=[endpoint_url, api_key],
            outputs=model_dropdown
        )
        api_key.change(
            fn=update_models,
            inputs=[endpoint_url, api_key],
            outputs=model_dropdown
        )

    return endpoint_url, api_key, model_dropdown