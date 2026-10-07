import requests

url = "https://jsonplaceholder.typicode.com/posts/9999"

resposta = requests.get(url)

if resposta.status_code == 200:
    print("Sucesso:", resposta.json())
else:
    print("Algo deu errado. Status:", resposta.status_code)