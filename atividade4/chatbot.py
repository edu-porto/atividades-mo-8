import gradio as gr

def greet(name):
    return "Olá " + name 

with gr.Blocks() as demo:
    name = gr.Textbox(label="Nome") 
    output = gr.Textbox(label="Resultado") 
    greet_btn = gr.Button("Cumprimentar") 
    greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet") 
    
demo.launch()