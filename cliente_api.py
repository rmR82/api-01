import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 5


class ErroDeApi(Exception):
    """Erro ao se comunicar com a API."""


def requisitar(metodo, caminho, **kwargs):
    url = f"{BASE_URL}{caminho}"
    try:
        resposta = requests.request(metodo, url, timeout=TIMEOUT, **kwargs)
        resposta.raise_for_status()
    except requests.exceptions.Timeout:
        raise ErroDeApi("A API demorou demais para responder.")
    except requests.exceptions.ConnectionError:
        raise ErroDeApi("Não foi possível conectar à API.")
    except requests.exceptions.HTTPError as erro:
        raise ErroDeApi(f"A API respondeu com erro: {erro}")
    except requests.exceptions.RequestException as erro:
        raise ErroDeApi(f"Erro inesperado: {erro}")

    if resposta.status_code == 204:
        return None
    return resposta.json()

def buscar_post(post_id):
    return requisitar("GET", f"/posts/{post_id}")


def listar_posts(user_id=None):
    params = {}
    if user_id is not None:
        params["userId"] = user_id
    return requisitar("GET", "/posts", params=params)


def criar_post(titulo, corpo, user_id):
    dados = {"title": titulo, "body": corpo, "userId": user_id}
    return requisitar("POST", "/posts", json=dados)


def listar_todos_paginado(por_pagina=10):
    todos = []
    pagina = 1
    while True:
        params = {"_page": pagina, "_limit": por_pagina}
        itens = requisitar("GET", "/posts", params=params)
        if not itens:
            break
        todos.extend(itens)
        pagina += 1
    return todos

if __name__ == "__main__":
    try:
        post = buscar_post(1)
        print("Título:", post["title"])

        posts_do_usuario = listar_posts(user_id=2)
        print("Posts do usuário 2:", len(posts_do_usuario))

        novo = criar_post("Meu post", "Conteúdo do post", 1)
        print("Criado com id:", novo["id"])

        todos = listar_todos_paginado()
        print("Total de posts:", len(todos))

        buscar_post(9999)
    except ErroDeApi as erro:
        print("Erro:", erro)