lista = [[], []]
temp = 0
for a in range(0, 7):
    temp = int(input(f'Digite o {a + 1}ª numero '))
    if temp % 2 == 0:
        lista[0].append(temp)
    else:
        lista[1].append(temp)
lista[0].sort()
lista[1].sort()
print(f'Os valores PARES digitados foram: {lista[0]}')
print(f'Os valores IMPARES digitados foram {lista[1]}')
