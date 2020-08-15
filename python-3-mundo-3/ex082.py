key = True
lista = []
pares = []
impares = [] 
while key == True:
    lista.append(int(input('Digite um número: ')))
    while True:
        sn = str(input('Deseja continuar?: [S][N]')).upper().strip()[0]
        if sn in 'SN':
            if sn in 'S':
                break
            elif sn in 'N':
                key = False
                break
            else:
                print('Opção invalida!',end='')
for a, b in enumerate(lista):
    if a % 2 == 0:
        pares.append(b)
    else:
        impares.append(b)
print(f'A lista COMPLETA é: {lista}')
print(f'A lista de PARES é: {pares}')
print(f'A lista de IMPARES é: {impares}')


    
        
