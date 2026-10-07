import requests

url = "https://jsonplaceholder.typicode.com/posts"

filtros = {"userId": 1, "userId": 3}

resposta = requests.get(url, params=filtros)

print("URL final:", resposta.url)
print("Status:", resposta.status_code)

posts = resposta.json()

print("Quantidade de posts do usuário 1:", len(posts))

for post in posts:
    print(post["id"], "-", post["title"])