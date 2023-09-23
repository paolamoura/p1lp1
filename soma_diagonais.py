def soma_diagonais(M):
    soma = 0
    for i in range(len(M)):
        for j in range(len(M)):
            if i == j or i + j == len(M) - 1:
                soma += M[i][j]

    return soma


M = [[1, 4],
     [0, 9]]
assert soma_diagonais(M) == 14
assert M == [[1, 4], [0, 9]]

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

assert soma_diagonais(M) == 25
assert M == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
