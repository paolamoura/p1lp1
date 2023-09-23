def is_in(el, lista):
    for e in lista:
        if e == el:
            return True
    return False


def uniq(lista):
    lista_unica = []
    for i in range(len(lista)):
        e1 = lista[i]
        tem_repetido = False
        for j in range(len(lista)):
            e2 = lista[j]
            if e1 == e2 and i != j:
                tem_repetido = True
                break
        if not tem_repetido:
            lista_unica.append(e1)
    return lista_unica


def unicos_em_comum(seq1, seq2):
    seq1_uniq = uniq(seq1)
    seq2_uniq = uniq(seq2)

    unicos = []

    for e1 in seq1_uniq:
        for e2 in seq2_uniq:
            if e1 == e2 and not is_in(e1, unicos):
                unicos.append(e1)

    return unicos


seq1 = ['A', 'A', 'B', 'C', 'C', 'D']
seq2 = ['B', 'A', 'C', 'D', 'D']
assert unicos_em_comum(seq1, seq2) == ['B']
seq1 = ['A', 'A', 'B', 'C']
seq2 = ['A', 'B', 'C']
assert unicos_em_comum(seq1, seq2) == ['B', 'C']

assert unicos_em_comum([], []) == []
