from random import randint
num = randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9),
print(f'Os valores sorteados foram: ',end='')
for a in num:
     print(a, end=' ')
print(f'\nO maior número sorteado foi: {max(num)}')
print(f'O menor número sorteado foi: {min(num)}')