def soma_triangulo_superior(matriz):
    soma = 0
    limite_linha = len(matriz) // 2
    for i in range(limite_linha):
        for j in range(len(matriz)):
            if i < j and j < len(matriz) - (i + 1):
                soma += matriz[i][j]
    return soma


M1 = [[10, 20, 30, 40, 50],
      [11, 21, 31, 41, 51],
      [12, 22, 32, 42, 52],
      [13, 23, 33, 43, 53],
      [14, 24, 34, 44, 55]]
assert soma_triangulo_superior(M1) == 121
