import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

alteracao = {
    "title": "Só o título mudou"
}

resposta = requests.patch(url, json=alteracao)

print("Status:", resposta.status_code)
print("Resposta:", resposta.json())