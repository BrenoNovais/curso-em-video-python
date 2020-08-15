n = int(input('Digite o número de termos: '))
print('Os primeiros elementos da da SEQUENCIA FIBONACCI de {} são:'.format(n))
t1 = 0
t2 = 1
cont = 3
print('{}, {}, '.format(t1, t2),end='')
while cont <= n:
    t3 = t1 + t2
    cont += 1
    print('{}, '.format(t3),end='')
    t1 = t2
    t2 = t3

