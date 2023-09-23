def diferenca_listas(lista1, lista2):
    for i in range(len(lista1)-1, -1, -1):
        for v in lista2:
            if lista1[i] == v:
                lista1.pop(i)
                break
    return lista1
