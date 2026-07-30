def soma(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma(lista[1:])

def conta(lista):
    if lista == []:
        return 0
    else:
        return 1 + conta(lista[1:])

def busca_maior(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    sub_max = busca_maior(lista[1:])
    return lista[0] if lista[0] > sub_max else sub_max

print(busca_maior([1,2,3,4,5]))