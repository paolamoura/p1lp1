palavra1 = input()
palavra2 = input()

menor_palavra = palavra1
if len(palavra1) > len(palavra2):
    menor_palavra = palavra2

print("Letras coincidentes")

letras_coincidentes = 0
for i in range(len(menor_palavra)):
    if palavra1[i] == palavra2[i]:
        print("'%s' na posição %d" % (palavra1[i], (i + 1)))
        letras_coincidentes += 1

porcentagem = 100 * (letras_coincidentes / (len(palavra1) + len(palavra2)))
print("Total de letras coincidentes: %d (%d%%)" %
      (letras_coincidentes, porcentagem))
