def elemento_faltando(lista1, lista2):
    elemento_faltando = None

    for el2 in lista2:
        achou = False
        for el1 in lista1:
            if el1 == el2:
                achou = True
                break
        if not achou:
            elemento_faltando = el2
            break

    return elemento_faltando


lista1 = [1, 2, 3, 4]
lista2 = [1, 2, 3, 4, 5]

assert elemento_faltando(lista1, lista2) == 5

lista1 = [4, 1, 2, 3]
lista2 = [6, 2, 3, 1, 4]

assert elemento_faltando(lista1, lista2) == 6

lista1 = [1]
lista2 = [1, 2]

assert elemento_faltando(lista1, lista2) == 2

lista1 = [1, 7, 6]
lista2 = [6, 4, 7, 1]

assert elemento_faltando(lista1, lista2) == 4

assert lista1 == [1, 7, 6]
assert lista2 == [6, 4, 7, 1]
