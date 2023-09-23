def elimina_kyw(sentenca):
    nova_sentenca = ''
    for c in sentenca:
        if c != 'k' and c != 'y' and c != 'w':
            nova_sentenca += c
    return nova_sentenca


s1 = 'kasayeww'
s2 = 'makria bonita'

assert elimina_kyw(s1) == 'asae'
assert elimina_kyw(s2) == 'maria bonita'
