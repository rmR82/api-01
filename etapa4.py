import requests

url = "https://jsonplaceholder.typicode.com/posts"

novo_post = {
    "title": "Meu primeiro post",
    "body": "Estou aprendendo a consumir APIs com Python.",
    "userId": 1,
    "categoria": "EStudo"
}

resposta = requests.post(url, json=novo_post)

print("Status:", resposta.status_code)
print("Resposta:", resposta.json())