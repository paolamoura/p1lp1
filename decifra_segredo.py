def decifra(chave, mensagem):
    msg_decifrada = ""
    for c in mensagem:
        msg_decifrada += chave[c]
    return msg_decifrada


chave1 = {'@': 'V', 'a': 'v', 'n': 'o', 'l': 'i', '#': ' ', '4': 'a', '+': 'u'}
assert decifra(chave1, '+a4') == 'uva'
assert decifra(chave1, '@nan#al+#4#+a4') == 'Vovo viu a uva'
