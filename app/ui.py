# main.py
# Gradio UI + App Entry Point

import gradio as gr

from app.llm_client import generate_tests
from app.test_runner import save_and_run_tests


def extract_code(text):
    """
    Remove markdown backticks if present
    """

    text = text.replace("```python", "")
    text = text.replace("```", "")

    return text.strip()


def generate_tests_code(code, module_name):
    """
    Main pipeline:
    1. Generate tests
    """

    if not code.strip():
        return "Please enter Python code"

    # Generate test code
    test_code = generate_tests(code, module_name)

    test_code = extract_code(test_code)

    return test_code

def run_tests(code, test_code, module_name):
    return  save_and_run_tests(
        code,
        test_code,
        module_name
    )

def launch_ui():

     # Build UI
    css = """
        textarea[rows]:not([rows="1"]) {
            overflow-y: auto !important;
            scrollbar-width: thin !important;
        }
        textarea[rows]:not([rows="1"])::-webkit-scrollbar {
            all: initial !important;
            background: #f1f1f1 !important;
        }
        textarea[rows]:not([rows="1"])::-webkit-scrollbar-thumb {
            all: initial !important;
            background: #a8a8a8 !important;
        }
        """

    with gr.Blocks() as app:

        gr.Markdown("## 🤖 AI Python Unit Test Generator")
        gr.Markdown("Generate Python unit tests for your code using Claude(Anthropic) LLM model.")
        with gr.Row():

            with gr.Column():
                code_input = gr.Textbox(
                    label="Python Code",
                    lines=15,
                    placeholder="Paste your Python function here..."
                )

                module_name = gr.Textbox(
                    label="Module Name",
                    value="mymodule"
                )

                generate_btn = gr.Button("🚀 Generate Tests")

            with gr.Column():
                test_output = gr.Textbox(
                    label="Generated Tests",
                    lines=15
                )
                run_btn = gr.Button("Run Tests")

            with gr.Column():
                result_output = gr.Textbox(
                    label="Pytest Output",
                    lines=10
                )

        generate_btn.click(
            generate_tests_code,
            inputs=[code_input, module_name],
            outputs=[test_output]
        )
        run_btn.click(
            run_tests,
            inputs=[code_input, test_output, module_name],
            outputs=[result_output]
        )
        app.launch(theme=gr.themes.Base(), css=css)
