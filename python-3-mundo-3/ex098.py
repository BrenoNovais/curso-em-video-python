from time import sleep
def contador(a, b, c):
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if c <= 0:
        c = 1
    if a > b:
        b += -1
        c = -c    
    for z in range(a, b, c):
        print(f'{z} ',end="", flush=True)
        sleep(0.1)
    print('FIM')


print('='*30)
print('Contagem de 1 até 10 de 1 em 1')
for z in range(1, 11):
    print(f'{z} ',end="", flush=True)
    sleep(0.1)
print('FIM')
print('='*30)
print('Contagem de 10 até 0 de 2 em 2')
for z in range(10, -1, -2):
    print(f'{z} ',end="")
    sleep(0.1)
print('FIM')
print('='*30)
print('Agora é sua vez de personalizar a contagem! ')

ini = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(ini, fim, passo)
    