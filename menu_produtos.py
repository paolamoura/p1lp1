def insere_produto(menu, produto, preco):
    menu.append((produto, preco))
    i = len(menu) - 1
    while menu[i - 1][1] > preco and i > 0:
        menu[i - 1], menu[i] = menu[i], menu[i - 1]
        i -= 1


menu = [("expresso", 5.29), ('duplo', 8.09), ('capuccino', 10.59)]
insere_produto(menu, 'latte', 9.59)

assert menu == [("expresso", 5.29), ('duplo', 8.09),
                ('latte', 9.59), ('capuccino', 10.59)]
