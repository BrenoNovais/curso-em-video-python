lista = 'Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,\
'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90,
t = len(lista)
a = 0
b = 1
print(f'{"LISTA DE PREÇO":-^39}')
while b <= t:
    print(f'{lista[a]:.<30}R${lista[b]: >7.2f}')
    a += 2
    b += 2


