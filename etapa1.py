import requests
url = "https://jsonplaceholder.typicode.com/posts/1"

resposta = requests.get(url)

dados = resposta.json()

print("Tipo de dados:", type(dados))
print("Título:", dados["title"])
print("ID do usuário:", dados["userId"])