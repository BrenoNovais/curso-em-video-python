from random import randint
from time import sleep
temp = []
jogo = []
quant = int(input('Quantos jogos você quer?'))
print(f'=-=-=-= SORTEANDO {quant} JOGOS =-=-=-=')
for a in range(0, quant):
    while len(temp) < 6:
        temp.append(randint(0, 60))
        for c in temp:
            if temp.count(c) > 1:
                temp.remove(c)
                
    sleep(0.5)
    temp.sort()
    print(f'Jogo {a + 1}: {temp}:')
    temp.clear()

print('=-=-=-=-= BOA SORTE =-=-=-=-=')