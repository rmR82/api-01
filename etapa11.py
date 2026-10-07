import requests

url = "https://httpbin.org/headers"

meus_headers = {
    "Accept": "application/json",
    "User-Agent": "meu-estudo-de-api/1.0",
    "X-Meu-Header": "teste123"
}

resposta = requests.get(url, headers=meus_headers, timeout=5)

print("Status:", resposta.status_code)
print(resposta.json()["headers"])
print("Content-Type da resposta:", resposta.headers["Content-Type"])
print("Todos os headers da resposta:", dict(resposta.headers))