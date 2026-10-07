import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

post_atualizado = {
    "id": 1,
    "title": "Título alterado",
    "body": "Conteúdo alterado com PUT.",
    "userId": 1
}

resposta = requests.put(url, json=post_atualizado)

print("Status:", resposta.status_code)
print("Resposta:", resposta.json())