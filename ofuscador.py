def primeiro_passo(linha):
    linha_obfuscada = ''
    for c in linha:
        if is_lower(c):
            linha_obfuscada += chr(ord(c) - 32)
        elif is_upper(c):
            linha_obfuscada += chr(ord(c) + 32)
        else:
            linha_obfuscada += c
    return linha_obfuscada


def segundo_passo(linha):
    linha_obfuscada = ''
    for c in linha:
        if c == 'a' or c == 'A':
            linha_obfuscada += '4'
        elif c == 'B' or c == 'b':
            linha_obfuscada += '8'
        elif c == 'G' or c == 'g':
            linha_obfuscada += '6'
        elif c == 'E' or c == 'e':
            linha_obfuscada += '3'
        elif c == 'I' or c == 'i':
            linha_obfuscada += '1'
        elif c == 'L' or c == 'l':
            linha_obfuscada += '7'
        elif c == 'S' or c == 's':
            linha_obfuscada += '5'
        elif c == 'O' or c == 'o':
            linha_obfuscada += '0'
        else:
            linha_obfuscada += c
    return linha_obfuscada


def terceiro_passo(linha):
    linha_obfuscada = ''

    tamanho_palavra_antes_do_espaco = 0
    for c in linha:
        if c != ' ':
            tamanho_palavra_antes_do_espaco += 1
            linha_obfuscada += c
        else:
            linha_obfuscada += '*' * tamanho_palavra_antes_do_espaco
            tamanho_palavra_antes_do_espaco = 0
    return linha_obfuscada


def is_lower(caracter):
    return 97 <= ord(caracter) <= 122


def is_upper(caracter):
    return 65 <= ord(caracter) <= 90


def ofuscador(linha):
    primeira_etapa = primeiro_passo(linha)
    segunda_etapa = segundo_passo(primeira_etapa)
    terceira_etapa = terceiro_passo(segunda_etapa)
    return terceira_etapa


linha = "I love Python!"
assert ofuscador(linha) == "1*70V3****pYTH0N!"
