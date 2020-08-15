from random import randint
from time import sleep
lista = []
lista2 = {}
soma = 0
def sorteia(* lista):
    for a in range(0, 5):
        num = randint(0, 10)
        lista2.copy(lista)
        print(f'{num}',end='')
    print(lista2)
print('PRONTO!')

def somapar(* lista):
        for a in range(lista):
            if a % 2 == 0:
                soma += a
print(f'Somando os valores pares de {lista} temos {soma}')


sorteia()
somapar()
