digitos = input()
limite = int(input())

soma = 0
num_impares = 0
i = 0

valido_limite = soma <= limite
valido_final = i < len(digitos)
valido_limite_impar = num_impares < 6
eh_valido = valido_final and valido_limite and valido_limite_impar
while eh_valido:
    digito = int(digitos[i])
    soma += digito
    num_impares += 1 if digito % 2 != 0 else 0
    i += 1

    valido_limite = soma <= limite
    valido_final = i < len(digitos)
    valido_limite_impar = num_impares < 6
    eh_valido = valido_final and valido_limite and valido_limite_impar

if not valido_limite:
    criterio_parada = "limite"
elif not valido_final:
    criterio_parada = "final da sequência"
else:
    criterio_parada = "6 ímpares"

print("soma: %d" % soma)
print("números lidos: %d de %d" % (i, len(digitos)))
print("critério de parada: %s" % criterio_parada)
