import gradio as gr
import os 
from openai import OpenAI

# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
)

# os.environ['OPENAI_API_TOKEN'] = 'sk-'

completion = client.chat.completions.create(
  model="gpt-3.5-turbo-0301",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)

# def greet(name):
#     return "Olá " + name 

# with gr.Blocks() as demo:
#     name = gr.Textbox(label="Nome") 
#     output = gr.Textbox(label="Resultado") 
#     greet_btn = gr.Button("Cumprimentar") 
#     greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet") 
    
# demo.launch()