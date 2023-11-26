import gradio as gr
from langchain.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableMap, RunnablePassthrough

model = Ollama(model='hokage')

prompt = ChatPromptTemplate.from_template("""
From now on you're an expert in industrial safety. Please be conscise on your answers and be extra cautions when giving tips on safety.
""")

chain = {"activity": RunnablePassthrough()} | prompt | model

def user_interaction(user_input, data_send):
    print("User sent : ", user_input)
    mensage = ""
    for s in chain.stream(user_input):
        print(s, end="", flush=True)
        mensage += s
        yield mensage




chatbot = gr.ChatInterface(user_interaction,
    chatbot=gr.Chatbot(height=700),
    textbox=gr.Textbox(placeholder="Ask me a question about industrial safety", container=False, scale=7),
    title='The safety expert',
    theme="soft",
    examples=["How i can climb a ladder safely ?",'How to cut a pipe with a circular saw ? '],
    cache_examples=False,
    retry_btn=None,
    undo_btn="Delete Previous",
    clear_btn="Clear"
    ).queue()

chatbot.launch()
