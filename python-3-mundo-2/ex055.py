maior = 0
menor = 0
for a in range(1, 6):
    peso = float(input('Digite 5 pesos? '))
    if a == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é: {}Kg'.format(maior))
print('O menor peso é: {}Kg'.format(menor))