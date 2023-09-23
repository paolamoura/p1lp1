jogadores = []
while True:
    jogador = input()
    if jogador == '-':
        break

    jogadores.append(jogador)

num_jogadores = len(jogadores)

if num_jogadores == 11:
    modalidade = 'Modalidade -> Futebol'
elif num_jogadores == 5:
    modalidade = 'Modalidade -> Basquete'
elif num_jogadores == 6:
    modalidade = 'Modalidade -> Vôlei'
elif num_jogadores == 7:
    modalidade = 'Modalidade -> Handebol'
else:
    modalidade = 'Equipe Inválida'

print(modalidade)
