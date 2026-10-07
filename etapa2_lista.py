import requests

resposta = requests.get("https://jsonplaceholder.typicode.com/posts")

posts = resposta.json()

print("Tipo:", type(posts))
print("Quantidade de posts:", len(posts))

for post in posts[:5]:
    print(post["id"], "-", post["title"])