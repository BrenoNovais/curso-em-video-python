lista = []
lista2 = [0, 0, 0, 1, 1, 1, 2, 2, 2]
lista3 = [0, 1, 2, 0, 1, 2, 0, 1, 2]
for a in range(0, 9):
    lista.append(int(input(f'Digite o valor para {lista2[a]}, {lista3[a]}: ')))
print(f'[ {lista[0]} ][ {lista[1]} ][ {lista[2]} ]')
print(f'[ {lista[3]} ][ {lista[4]} ][ {lista[5]} ]')
print(f'[ {lista[6]} ][ {lista[7]} ][ {lista[8]} ]')
