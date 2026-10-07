import requests

url = "https://jsonplaceholder.typicode.com/posts/9999"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()
    print("Sucesso:", resposta.json())
except requests.exceptions.HTTPError as erro:
    print("Erro HTTP:", erro)