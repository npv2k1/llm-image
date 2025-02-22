import gradio as gr

from src.modules.gradio_app.components.config_panel import create_config_panel
from src.modules.gradio_app.components.prompt_panel import create_prompt_panel
from src.modules.gradio_app.components.image_panel import create_image_panel
from src.modules.gradio_app.utils.analysis import analyze_image

def create_gradio_app():
    """Create the main Gradio application with all components"""
    with gr.Blocks() as app:
        gr.Markdown("# Image Analysis with LLM")
          # Image Analysis Panel
        image_input, analyze_button, output = create_image_panel()

        # Configuration Panel
        with gr.Row():
            endpoint_url, api_key, model_dropdown = create_config_panel()

        # Prompt Panel
        with gr.Row():
            prompt_input, system_prompt, temperature = create_prompt_panel()

      
        # Connect the analyze button to the analysis function
        analyze_button.click(
            fn=analyze_image,
            inputs=[
                image_input,
                endpoint_url,
                api_key,
                model_dropdown,
                prompt_input,
                system_prompt,
                temperature
            ],
            outputs=output
        )
        
    return app

app = create_gradio_app()

# Configure server settings for Docker deployment
server_port = 7860  # Standard Gradio port
server_name = "0.0.0.0"  # Allow external connections

def main():
    """Launch the Gradio application"""
    app.launch(
        server_name=server_name,
        server_port=server_port,
        share=False,  # Disable sharing as we're running in Docker
        auth=None,    # Can be configured if authentication is needed
        ssl_verify=False,  # Disable SSL verification for internal Docker network
        show_error=True,
        favicon_path=None
    )

main()