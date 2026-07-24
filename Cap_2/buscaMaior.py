def buscaMaior(arr):
    maior = arr[0]
    maior_indice = 0
    for i in range (1,len(arr)):
        if arr[i] > maior:
            maior = arr[i]
            maior_indice = i
    return maior_indice

def ordenacaoporSelecao(arr):
    novoArr = []
    for i in range (len(arr)):
        maior = buscaMaior(arr)
        novoArr.append(arr.pop(maior))
    return novoArr

print(ordenacaoporSelecao([5,3,6,2,10]))