pos = 'um', 'outro', 'mais um', 'o ultimo'
num1 = ()
contp = ()
cont = p3 = 0
for a in pos:
    num = int(input(f'Digite {a} número:'))
    num1 += num,
    cont += 1
    if num % 2 == 0:
        contp += num,
    if num == 3:
        p3 = cont
print(f'Você digitou os valores {num1}')
print(f'O valor 9 apareceu {num1.count(9)} vezes.')
if p3 != 0 :
    print(f'O valor 3 apareceu na {p3}ª posição.')
else:
    print('O numero 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram {contp}')