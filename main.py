from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

numero_dias = 7
numero_criancas = 2
atividade = "praia"

modelo_de_promt = PromptTemplate(
    template="""
    Crie um roteiro de viagem de {dias} dias,
    para uma família com {numero_criancas} crianças,
    que gostam de {atividade}.
    """
)

prompt = modelo_de_promt.format(
    dias=numero_dias,
    numero_criancas=numero_criancas,
    atividade=atividade
)

modelo = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.5,
    api_key=api_key
)

resposta = modelo.invoke(prompt)
print(resposta.content)