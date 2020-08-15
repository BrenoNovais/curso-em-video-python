from random import randint
lista2 = {}
lista = []

def random():
    print(f'Sorteando os valores da lista: ',end='')
    for a in range(0, 5):
        lista.append(randint(0, 10))
        print(f'{lista[a]} ',end='')
    print('PRONTO!')


def par(a):
    somapar = 0
    for b, c in enumerate(a):
        if c % 2 == 0:
            somapar += c
    print(f'Somando os valores pares de: {a}, temos {somapar}')

random()
par(lista)
