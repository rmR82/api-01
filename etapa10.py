import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    resposta = requests.get(url, timeout=5)
    resposta.raise_for_status()
    print("Sucesso:", resposta.json())
except requests.exceptions.Timeout:
    print("A API demorou demais para responder.")
except requests.exceptions.ConnectionError:
    print("Não foi possível conectar. Verifique a internet ou o endereço.")
except requests.exceptions.HTTPError as erro:
    print("Erro HTTP:", erro)
except requests.exceptions.RequestException as erro:
    print("Erro inesperado na requisição:", erro)