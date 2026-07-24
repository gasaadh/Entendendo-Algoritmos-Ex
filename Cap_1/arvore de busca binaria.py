def cria_no(valor):
    return {"valor": valor, "esquerda": None, "direita": None}

def inserir(raiz, valor):
    if raiz is None:
        return cria_no(valor)

    if valor < raiz["valor"]:
        raiz["esquerda"] = inserir(raiz["esquerda"], valor)
    else:
        raiz["direita"] = inserir(raiz["direita"], valor)

    return raiz

def buscar(raiz, item):
    if raiz is None:
        return False          # chegou numa "folha vazia" e não achou
    if raiz["valor"] == item:
        return True
    elif item < raiz["valor"]:
        return buscar(raiz["esquerda"], item)
    else:
        return buscar(raiz["direita"], item)


# montando a árvore
minha_arvore = None
for numero in [5, 3, 7, 1, 9]:
    minha_arvore = inserir(minha_arvore, numero)

print(buscar(minha_arvore, 9))   # True
print(buscar(minha_arvore, 4))   # False