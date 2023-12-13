import gradio as gr
import numpy as np
from openai import OpenAI
import os 
from dotenv import load_dotenv

# Pegando a chave da API no .env
load_dotenv()
chat_key = os.getenv("KEY")


client = OpenAI(api_key = chat_key)

# Aqui o áudio é transformado em texto. O padrão é PT-BR  
def transcribe(audio_path):
    true_path = str(audio_path)
    audio_file = open(f"{true_path}.m4a", "rb")
    transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file,
    response_format = "text")
    return transcript


# Traduzindo o input de PT-BR para Italiano  
def translate(text_input): 
    user_input = text_input
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "system",
        "content": "Você vai receber um texto em Português e sua função é traduzir para Italiano "
        },
        {
        "role": "user",
        "content": user_input
        }
    ],
    temperature=0.7
    )
    translated_text = response.choices[0].message.content
    return translated_text

# Aqui o texto é convertido para voz 
def text_to_voice(text_input):
    true_input = str(text_input)
    response = client.audio.speech.create(
    model="tts-1",
    voice="onyx",
    input=true_input,)
    response.stream_to_file("output.mp3")


if __name__ == "__main__":
    # Aqui o usuario vai inputar o nome do arquivo 
    user_input = input("Digite o nome do arquivo de áudio : ")

    stt = transcribe(user_input)

    print("------------- Mostrando o Speech to Text -------------")
    print("")
    print(stt)

    translation_pt_it = translate(stt)
    
    print("")
    print("------------- Mostrando a tradução do STT -------------")
    print("")
    print(translation_pt_it)

    audio_final = text_to_voice(translation_pt_it)
    print("")
    print("------------- Para conferir a tradução em voz acesso o arquivo 'output.mp3'  -------------")
    print("")
