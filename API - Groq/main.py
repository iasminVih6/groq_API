# Flask: framework que cria a API (as "rotas" que respondem a requisições HTTP)
from flask import Flask, request, jsonify

# OpenAI: biblioteca cliente que vamos "enganar" pra falar com o Groq
from openai import OpenAI

# Lê as variáveis do arquivo .env e coloca elas disponíveis pro os.environ
from dotenv import load_dotenv
import os

load_dotenv()  # executa a leitura do .env — sem isso, os.environ não acha a chave

# Cria o "app" — a instância principal da nossa API
app = Flask(__name__)

# Cria o cliente que vai conversar com o Groq
# api_key: a chave secreta, lida da variável de ambiente
# base_url: aponta pro servidor do Groq em vez do servidor da OpenAI (é essa a "mágica")
client = OpenAI(
    api_key=os.environ["Chave_GROQ"],
    base_url="https://api.groq.com/openai/v1"
)

# Define uma rota: quando alguém mandar um POST para /perguntar, essa função roda
@app.route("/perguntar", methods=["POST"])
def perguntar():
    # Pega o JSON que a pessoa mandou no corpo da requisição
    # exemplo esperado: { "pergunta": "o que é uma API?" }
    dados = request.get_json()

    # Pega o valor da chave "pergunta" dentro desse JSON
    pergunta = dados.get("pergunta")

    # Validação simples: se não veio pergunta, devolve erro 400 (pedido inválido)
    if not pergunta:
        return jsonify({"erro": "envie uma 'pergunta' no corpo da requisição"}), 400

    # Manda a pergunta pra IA do Groq e espera a resposta
    resposta = client.chat.completions.create(
        model="openai/gpt-oss-20b",   # qual modelo de IA vai responder
        messages=[{"role": "user", "content": pergunta}]  # a "conversa" — só a pergunta do usuário
    )

    # Extrai só o texto da resposta (o resto do objeto tem metadados que não precisamos agora)
    texto_resposta = resposta.choices[0].message.content

    # Devolve pro usuário um JSON simples com a resposta
    return jsonify({"resposta": texto_resposta})

# Só roda o servidor se este arquivo for executado diretamente (não se for importado)
if __name__ == "__main__":
    app.run(debug=True)  # debug=True reinicia o servidor sozinho quando você salva o arquivo