def maior_slice(lista):
    maior_sublista_crescente = []
    for i in range(len(lista)):
        sublista = [lista[i]]
        k = 0
        for j in range(i + 1, len(lista)):
            if lista[j] > sublista[k]:
                sublista.append(lista[j])
                k += 1
            else:
                break
        if len(sublista) >= len(maior_sublista_crescente):
            maior_sublista_crescente = sublista
    return maior_sublista_crescente


assert maior_slice([1, 2, 3, 4, 2, 0, 1]) == [1, 2, 3, 4]
assert maior_slice([7, 6, 2, 9, 10]) == [2, 9, 10]
assert maior_slice([7, 8, 9, 1, 2, 3, 0]) == [1, 2, 3]
