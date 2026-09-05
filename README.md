# LangChain e Python: criando ferramentas com o Groq

## ⚙️ Guia de Configuração

Siga os passos abaixo para configurar seu ambiente e utilizar os scripts do projeto.

### 1. Criar e Ativar Ambiente Virtual

**Windows:**
```bash
python -m venv .venv
langchain\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv .venv
source langchain/bin/activate
```

### 2. Instalar Dependências

Utilize o comando abaixo para instalar as bibliotecas necessárias:
```bash
pip install -r requirements.txt
```

### 3. Configurar Chave do Groq

Crie ou edite o arquivo `.env` adicionando sua chave de API da OpenAI:
```bash
GROQ_API_KEY="SUA_CHAVE_DE_API"
```
