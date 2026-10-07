import os

import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("API_TOKEN")

if token is None:
    print("Token não encontrado. Verifique o arquivo .env")
else:
    url = "https://httpbin.org/bearer"
    headers = {"Authorization": f"Bearer {token}"}

    resposta = requests.get(url, headers=headers, timeout=5)

    print("Status:", resposta.status_code)
    print("Resposta:", resposta.json())