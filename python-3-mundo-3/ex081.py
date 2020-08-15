lista = []
resp = ''
key = True
while key == True:
    lista.append(int(input('Digite um numero para lista: ')))
    while True:
        resp = str(input('Deseja continuar?')).upper().strip()[0]
        if resp in 'SN':
            if resp in 'S':
                break
            elif resp in 'N':
                key = False
                break
            else:
                print('Resposta invalida')
print(f'{len(lista)} Números foram digitados')
lista.sort(reverse=True)
print(f'{lista}')
if lista.count(5) == 0:
    print('O valor 5 não esta na lista')
else:
    print('O valor 5 esta na lista')

