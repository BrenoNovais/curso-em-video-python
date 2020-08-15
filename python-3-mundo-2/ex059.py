from time import sleep
print('=-='*20)
exit = 'exit'
confirm = ''
maior = 0
num1 = int(input('Digite um número:'))
num2 = int(input('Digite outro numero'))
print('=-=' * 20)

while exit != confirm:
    menu = input(''' Bem vindo ao menu, para:
    Somar, Digite[1]
    Multiplicar  [2]
    Saber maior  [3]
    Novos números[4]
    Sair do APP  [5]
    ''')
    if menu == '1':
        print('=-=' * 20)
        soma = num1 + num2
        print('A soma de {} e {} é: {}'.format(num1, num2, soma))
        print('=-=' * 20)
    if menu == '2':
        print('=-=' * 20)
        mult = num1 * num2
        print('A multiplicação de {} X {} é {}'.format(num1, num2, mult))
        print('=-=' * 20)
    if menu == '3':
        print('=-=' * 20)
        if num1 > num2:
            maior += num1
        else:
            maior += num2
        print('O maior número entre {} e {} é: {}'. format(num1, num2, maior))
        print('=-=' * 20)
    if menu == '5':
        print('=-=' * 20)
        confirm += 'exit'
    if menu == '4':
        print('Você decidiu escolher novos números')
        num1 = int(input('Digite um número:'))
        num2 = int(input('Digite outro numero'))
        print('=-=' * 20)
    sleep(2)

print('=-='*20)
print('Você saiu do APP')

