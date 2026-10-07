import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

resposta = requests.delete(url)

print("Status:", resposta.status_code)
print("Resposta:", resposta.json())