import gradio as gr
from llmlingua import PromptCompressor

llm_lingua = PromptCompressor("lgaalves/gpt2-dolly", device_map="cpu")

intro = """
<img src="https://seonotebook.com/wp-content/uploads/2020/07/seonotebook-logo-rgb.png" width="250">

# SEO Notebook Prompt Compressor

Uses [LLMLingua](https://github.com/microsoft/LLMLingua) to compress a prompt to a target token length or a target compression ratio.

### How to use
1. Enter the context, instruction, and question in the respective text boxes.
2. Enter the compression ratio or target token length.
3. Click the "Compress Prompt" button.
4. The compressed prompt, original tokens, compressed tokens, actual compression ratio, and saving cost will be displayed.
"""


def compress_prompt(context, instruction, question, ratio, target_token):
    context, instruction, question = context.replace("\\n", "\n"), instruction.replace("\\n", "\n"), question.replace("\\n", "\n")
    compressed_prompt = llm_lingua.compress_prompt(context.split("\n\n"), instruction, question, float(ratio), float(target_token))

    return [compressed_prompt[key] for key in ["compressed_prompt", "origin_tokens", "compressed_tokens", "ratio", "saving"]]
    
custom_css = """
    #image-upload {
        flex-grow: 1;
    }
    #params .tabs {
        display: flex;
        flex-direction: column;
        flex-grow: 1;
    }
    #params .tabitem[style="display: block;"] {
        flex-grow: 1;
        display: flex !important;
    }
    #params .gap {
        flex-grow: 1;
    }
    #params .form {
        flex-grow: 1 !important;
    }
    #params .form > :last-child{
        flex-grow: 1;
    }
    .md ol, .md ul {
        margin-left: 1rem;
    }
    .md img {
        margin-bottom: 1rem;
    }
"""

with gr.Blocks(title="SEO Notebook Promp Compressor", css=custom_css, theme=gr.themes.Soft_SNB()) as iface:
    gr.Markdown(intro)

    with gr.Row():
        with gr.Column(elem_id="prompt", scale=2):
            instruction = gr.Textbox(label="Instruction", placeholder="This module consists of directives given by the user to the LLMs, such as task descriptions.")
            context = gr.Textbox(
                                label="Context", 
                                placeholder="This module provides the supplementary context needed to address the question, such as documents, demonstrations, web search results, or API call results.",
                                lines=10
                                )
            question = gr.Textbox(label="Question", placeholder="This refers to the directives given by the user to the LLMs, such as inquiries, questions, or requests.", lines=3)

        with gr.Column(elem_id="params", scale = 1):
            ratio = gr.Textbox(label="Compression Ratio (To use this, set Target Token to -1)", value=0)
            target_token = gr.Textbox(label="Target Token (To use this, set Compression Ratio to 0)", value=200)

    submit_button = gr.Button(value="Compress Prompt", variant="primary")

    with gr.Row():
        with gr.Column(elem_id="Results", scale=2):
            output = gr.Textbox(label="Compressed Prompt", lines=15)
        with gr.Column(elem_id="Results", scale=1):
            origin_tokens = gr.Textbox(label="The tokens number of original prompt")
            compressed_tokens = gr.Textbox(label="The tokens number of compressed prompt")
            saving_ratio = gr.Textbox(label="Actual Compression Ratio")
            saving = gr.Textbox(label="Saving Cost")

    submit_button.click(
        fn=compress_prompt, 
        inputs=[
            context,
            instruction,
            question,
            ratio,
            target_token
        ],
        outputs=[
            output,
            origin_tokens,
            compressed_tokens,
            saving_ratio,
            saving
        ]
    )

iface.launch()