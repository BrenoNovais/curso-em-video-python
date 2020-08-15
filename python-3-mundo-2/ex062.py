num1 = int(input('Digite o PRIMEIRO TERMO da P.A:'))
num2 = int(input('Digite a RAZAO da P.A'))
print('='*33)
soma = num1 + 10 * num2
resp = 0
termos = 10
print('A P.A com PRIMEIRO TERMO {} e RAZÃO {} é:'.format(num1, num2))
fim = 0
while num1 < soma:
    print('{} '.format(num1), end='')
    num1 += num2
while fim < 1:
    print('\nMais quantos TERMOS você quer ver?')
    resp += int(input('Para finalizar: Digite [0]\n================================='))
    if resp != 0:
        print('Os outros {} TERMOS pedidos são:'.format(resp))
        termos += resp
        soma2 = num1 + resp * num2
        while num1 < soma2:
            print('{} '.format(num1),end='')
            num1 += num2
            resp *= 0
    else:
        fim += 1
print('='*33)
print('{} Termos foram mostrados'.format(termos))
print('Operação finalizada!')
print('='*33)
