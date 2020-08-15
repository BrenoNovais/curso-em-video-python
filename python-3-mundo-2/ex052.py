num = int(input('Digite um numero: '))
total = 0
for a in range(1, num + 1):
    if num % a == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(a), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes'.format(num, total))
if a % 2 == 0:
    print('{} NÃO É NÚMERO PRIMO'.format(num))
else:
    print('{} É NÚMERO PRIMO'.format(num))