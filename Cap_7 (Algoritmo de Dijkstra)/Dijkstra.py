grafo = {}

grafo["inicio"] = {}

grafo["inicio"]["A"] = 6
grafo["inicio"]["B"] = 2

grafo["A"] = {}
grafo["A"]["fim"] = 1

grafo["B"] = {}
grafo["B"]["A"] = 3
grafo["B"]["fim"] = 5

grafo["fim"] = {}


"""Tabela Hash de Custos"""

infinito = float("inf")
custos = {}
custos["A"] = 6
custos["B"] = 2
custos["fim"] = infinito

"""Tabela Hash para os Pais"""
pais = {}
pais["A"] = "inicio"
pais["B"] = "inicio"
pais["fim"] = None

processados = []

nodo = ache_no_custo_mais_baixo(custos)
while nodo != None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = nodo
    processados.append(nodo)
    nodo = ache_no_custo_mais_baixo(custos)


def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None
    for nodo in custos:
        custo = custos[nodo]
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
        return nodo_custo_mais_baixo


print(grafo["inicio"].keys())

print(grafo["inicio"]["A"])
print(grafo["inicio"]["B"])