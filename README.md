# API Groq — Estudo

Uma API simples em Python que recebe uma pergunta e devolve a resposta gerada por um modelo de IA, usando a [Groq](https://console.groq.com).

Feita como projeto de estudo para entender, na prática, como funciona a integração de uma API própria com uma API de IA externa.

## Como funciona

```
Você → POST /perguntar → Flask → Groq (IA) → resposta → você
```

1. Você manda uma pergunta em texto para a rota `/perguntar`.
2. O Flask recebe, valida e repassa a pergunta para a Groq.
3. A Groq processa com um modelo de IA e devolve uma resposta.
4. O Flask extrai o texto da resposta e devolve para você em JSON.

## Tecnologias

- **Python 3.11**
- **Flask** — framework que cria a API
- **openai (lib)** — usada para falar com a Groq, já que a Groq segue o mesmo padrão de API da OpenAI
- **python-dotenv** — carrega a chave secreta a partir de um arquivo `.env`

## Estrutura do projeto

```
API - Groq/
├── main.py           # todo o código da API
├── .env               # guarda a chave da Groq
└── requirements.txt   # dependências do projeto
```

## Como rodar

### 1. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 2. Criar sua chave da Groq
- Crie uma conta em [console.groq.com](https://console.groq.com)
- Vá em **API Keys** → **Create API Key**
- Copie a chave gerada

### 3. Criar o arquivo `.env`
Na raiz do projeto, crie um arquivo `.env` com:
```
GROQ_API_KEY=sua_chave_aqui
```

### 4. Rodar o servidor
```bash
python main.py
```
O servidor sobe em `http://127.0.0.1:5000`.

### 5. Testar a rota

No PowerShell:
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/perguntar" -Method Post -ContentType "application/json" -Body '{"pergunta": "o que e uma API em uma frase?"}'
```

Resposta esperada:
```json
{ "resposta": "Uma API é uma interface que permite que dois sistemas se comuniquem." }
```

## Modelo usado

```python
model="openai/gpt-oss-20b"
```
> A Groq atualiza sua lista de modelos disponíveis com frequência. Se aparecer o erro `model_not_found`, confira a lista atual em `console.groq.com/docs/models`.

## Próximos passos possíveis
- Guardar o histórico de perguntas/respostas em um arquivo ou banco
- Como ainda está em um estado inicial de testes, não utilize perguntas com acentos, pois dá erro
- Deixar a resposta em streaming (aparecendo aos poucos)
- Adicionar um front-end simples para não depender de `curl`/`Invoke-RestMethod`
