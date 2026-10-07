import requests

url = "https://httpbin.org/bearer"

token = "meu_token_de_teste_123"

headers = {
    "Authorization": f"Bearer {token}"
}

resposta = requests.get(url, headers=headers, timeout=5)

print("Status:", resposta.status_code)
print("Resposta:", resposta.json())