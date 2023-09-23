def is_in(el, estoque):
    for k in estoque.keys():
        if el == k:
            return True
    return False


def adiciona_estoque(estoque, novo_estoque):
    for k, v in estoque.items():
        if is_in(k, novo_estoque):
            novo_estoque[k] += v
        else:
            novo_estoque[k] = v
    return novo_estoque


def balanco(estoque1, estoque2):
    novo_estoque = {}
    novo_estoque = adiciona_estoque(estoque1, novo_estoque)
    return adiciona_estoque(estoque2, novo_estoque)


d1 = {"manteiga": 10, "biscoito": 20, "chocolate": 30}
d2 = {"manteiga": 10, "gelatina": 40}
assert balanco(d1, d2) == {"manteiga": 20, "biscoito": 20,
                           "chocolate": 30, "gelatina": 40}
assert d1 == {"manteiga": 10, "biscoito": 20, "chocolate": 30}
assert d2 == {"manteiga": 10, "gelatina": 40}
