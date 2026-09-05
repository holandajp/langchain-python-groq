from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

numero_dias = 7
numero_criancas = 2
atividade = "praia"

prompt = f"Crie um roteiro de viagem, para um período de {numero_dias}, para uma família com {numero_criancas} que busca atividades relacionadas a {atividade}"

modelo = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.5,
    api_key=api_key
)

resposta = modelo.invoke(prompt)
print(resposta.content)