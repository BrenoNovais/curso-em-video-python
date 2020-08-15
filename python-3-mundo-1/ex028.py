from random import randint
num = randint(0, 5)
num2 = float(input('Digite um número'))
print('processando...')

if num2 == int(num):
    print('você acertou, eu pensei no número',num)
else:
    print('Você errou, eu pensei no número',num)



