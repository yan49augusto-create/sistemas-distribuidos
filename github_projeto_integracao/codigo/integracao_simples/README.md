Projeto mínimo de integração entre APIs (versão super simples)

Arquivos:
- api_validadora.py  -> API B (validadora) - FastAPI
- cliente.py         -> cliente que envia requisições - requests
- requirements_validator.txt
- requirements_client.txt

Como executar:

1) Rodar a API validadora (manter em execução):
   pip install -r requirements_validator.txt
   uvicorn api_validadora:app --reload --host 0.0.0.0 --port 8000

2) Em outro terminal, rodar o cliente:
   pip install -r requirements_client.txt
   python cliente.py

O cliente enviará 3 requisições de exemplo:
- payload válido (esperado 200)
- chave inválida (esperado 401)
- payload inválido (esperado 400)
