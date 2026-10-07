import requests

url = "https://jsonplaceholder.typicode.com/posts"

todos = []
pagina = 1

while True:
    params = {"_page": pagina, "_limit": 10}
    resposta = requests.get(url, params=params, timeout=5)
    resposta.raise_for_status()

    itens = resposta.json()

    if not itens:
        break

    todos.extend(itens)
    print(f"Página {pagina}: {len(itens)} itens")
    pagina += 1

print("Total coletado:", len(todos))