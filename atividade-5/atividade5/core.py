from langchain.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough
from langchain.document_loaders import TextLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader
import gradio as gr


# Carrega o documento e o divide para usar como contexto
loader = TextLoader("./data/rules.txt")
documents = loader.load()

# Divide em chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# create the open-source embedding function
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# load it into Chroma
vectorstore = Chroma.from_documents(docs, embedding_function)

retriever = vectorstore.as_retriever()

template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

model = Ollama(model="eike")

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
)


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
    title='The expert in workshop safety ',
    theme="soft",
    examples=["AM i allowed to eat inside the workshop ?",'What i have to do to use some paint ? '],
    cache_examples=False,
    retry_btn=None,
    undo_btn="Delete Previous",
    clear_btn="Clear"
    ).queue()

chatbot.launch()

