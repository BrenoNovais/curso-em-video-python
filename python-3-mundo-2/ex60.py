soma = 1
print('Leitor de Fatorial')
num = int(input('Digite um número'))
print('O Fatotial de {} é: {}!='.format(num, num), end='')
for num2 in range(num, 0, -1):
    soma *= num2
    print('{}'.format(num2), end='x')
print('={}'.format(soma))
fat = ''
num3 = int(input('Digite um número')) + 1
print('O Fatorial de {} é: {}!='.format(num3 - 1, num3 - 1), end='')
soma2 = 1
while fat != 'ok':
    num3 += -1
    soma2 *= num3
    print('x{}'.format(num3), end='')
    if num3 == 1:
        fat += 'ok'
print('={}'.format(soma2))