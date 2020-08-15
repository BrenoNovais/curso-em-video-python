from random import randint
from time import sleep
from operator import itemgetter
ranking = []
jogadores = {'Jogador1':randint(0, 6),
             'Jogador2':randint(0, 6),
             'Jogador3':randint(0, 6),
             'Jogador4':randint(0, 6)}
print('Valores sorteados:')
for k, v in jogadores.items():  
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(jogadores)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar {v[0]} com {v[1]}')