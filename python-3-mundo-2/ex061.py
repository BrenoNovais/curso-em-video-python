num1 = int(input('Digite o PRIMEIRO TERMO da P.A:'))
num2 = int(input('Digite a RAZAO da P.A'))
soma = num1 + 10 * num2
print('A P.A com PRIMEIRO TERMO {} e RAZÃO {} é:'.format(num1, num2))
while num1 < soma:
    print('{} '.format(num1), end='')
    num1 += num2
