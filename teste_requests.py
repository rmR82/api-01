import requests

url = "https://jsonplaceholder.typicode.com/posts/9999"

resposta = requests.get(url)

print("Status:", resposta.status_code)
print("Corpo:", resposta.text)