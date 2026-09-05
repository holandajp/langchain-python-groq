from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.tracers.stdout import ConsoleCallbackHandler
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from pydantic import Field, BaseModel
from dotenv import load_dotenv
from langchain.globals import set_debug
import os

set_debug(True)

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

class Destino(BaseModel):
    cidade:str = Field("A cidade recomendada para visitar")
    motivo:str = Field("motivo pelo qual é interessante visitar essa cidade")

parseador = JsonOutputParser(pydantic_object=Destino)

prompt_cidade = PromptTemplate(
    template="""
    Sugira uma cidade dado o meu interesse por {interesse}.
    {formato_de_saida}
    """,    
    input_variables=["interesse"],
    partial_variables={"formato_de_saida": parseador.get_format_instructions()}
)

modelo = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.5,
    api_key=api_key
)

cadeia = prompt_cidade | modelo | parseador

resposta = cadeia.invoke(
    {
        "interesse" : "praias"
    },
    config={
        "callbacks": [ConsoleCallbackHandler()]
    }
)
print(resposta)