print('=-='*15)
lista = []
temp = 0
lista2 = [0, 0, 0, 1, 1, 1, 2, 2, 2]
lista3 = [0, 1, 2, 0, 1, 2, 0, 1, 2]
pares = tc = sl = 0
for a in range(0, 9):
    temp = int(input(f'Digite o valor para {lista2[a]}, {lista3[a]}: '))
    lista.append(temp)
    if temp % 2 == 0:
        pares += temp
    if a == 2 or a == 5 or a == 8:
        tc += temp
        print(temp)
    if a == 3:
        sl = temp
    if a == 4 or 5 and temp > sl:
        sl = temp
    
print(f'[ {lista[0]} ][ {lista[1]} ][ {lista[2]} ]')
print(f'[ {lista[3]} ][ {lista[4]} ][ {lista[5]} ]')
print(f'[ {lista[6]} ][ {lista[7]} ][ {lista[8]} ]')
print('=-='*15)
print(f'A soma dos valores pares é: {pares}')
print(f'A soma dos valores da terceira coluna é {tc}')
print(f'O maior valor da segunda linha é: {sl}')