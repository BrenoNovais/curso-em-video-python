num = int(input('Digite um numero inteiro.'))
print('Qual sera a base de conversão?')
base =(int(input('Digite:\nPara binário [1]\nPara Octal [2] \nPara hexadecimal [3]')))
if base == 1:
    print('{} Convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} Convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} Convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))

