import requests
import json

URL = "http://localhost:8000/validar"
CORRECT_KEY = "1234"
WRONG_KEY = "0000"

def send(nome, idade, api_key=CORRECT_KEY):
    headers = {"api_key": api_key, "Content-Type": "application/json"}
    payload = {"nome": nome, "idade": idade}
    resp = requests.post(URL, json=payload, headers=headers)
    try:
        data = resp.json()
    except Exception:
        data = {"status":"erro","mensagem":"Resposta não-JSON","text":resp.text}
    print(f"HTTP {resp.status_code} -> {json.dumps(data, ensure_ascii=False)}")

if __name__ == '__main__':
    print("1) Enviando payload válido")
    send("Yan", 20, CORRECT_KEY)

    print("\n2) Enviando com API Key inválida")
    send("Yan", 20, WRONG_KEY)

    print("\n3) Enviando payload inválido (idade texto)")
    send("Yan", "vinte", CORRECT_KEY)
