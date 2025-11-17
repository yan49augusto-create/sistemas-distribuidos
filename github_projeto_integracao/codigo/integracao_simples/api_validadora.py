from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

API_KEY = "1234"

@app.post("/validar")
def validar(dados: dict, api_key: str = Header(None)):
    # Verifica API Key
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail={"status":"erro","mensagem":"API Key inválida"})

    # Verifica campos obrigatórios
    if "nome" not in dados or "idade" not in dados:
        raise HTTPException(status_code=400, detail={"status":"erro","mensagem":"Dados incompletos"})

    return {"status": "sucesso", "mensagem": "Dados válidos", "dados_recebidos": dados}
