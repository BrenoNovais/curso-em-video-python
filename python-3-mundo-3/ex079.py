lista = []
ver = True
while ver == True:
    lista.insert(0, (int(input('Digite um valor: '))))
    lista2 = lista[0]
    if lista.count(lista2) > 1:
        print('Valor duplicado, não vou adicionar!')
        lista.pop(0)
    else:
        print('Valor adicionado com sucesso...')
    while True:
        confirm = str(input('Quer continuar? [S][N]')).upper().split()[0]
        if confirm == 'S':
            break
        if confirm == 'N':
            ver = False
            break
        else:
            print('Resposta invalida, ',end='')
lista.sort()
print(f'Os valores unicos digitados foram {lista}')