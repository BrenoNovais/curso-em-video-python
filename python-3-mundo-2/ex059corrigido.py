from math import factorial
num = int(input('Digite um número'))
c = num
f = 1
while c > 0:
    print('{}!'.format(num),end='')
    print(' x ' if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print('{}'.format(f))


num2 = int(input('Digite um número'))
fe = factorial(num2)
print('O fatorial de {} é {}'.format(num2, fe))



