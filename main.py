from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

numero_dias = 7
numero_criancas = 2
atividade = "música"

prompt = f"Crie um roteiro de viagem de {numero_dias}, para uma família com {numero_criancas}, que gosta de {atividade}."

cliente = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

resposta = cliente.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role" : "system",
            "content" : "Você é um assistente de roteiro de viagens"
        },
        {
            "role" : "user",
            "content" : prompt
        }
    ]
)

resposta_em_texto = resposta.choices[0].message.content
print(resposta_em_texto)