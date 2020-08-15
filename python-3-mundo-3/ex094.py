info = {}
infotemp = []
mulheres = []
confirm = nome = sexo =  ''
cont = idade = media = media2 = 0
while True:
    nome = str(input('Nome: '))
    while True:
        sexo = str(input('Sexo: [M][F]')).upper().split()[0]
        if sexo in 'MF':
            break
        else:
            print('Sexo invalido!')
    if sexo in 'fF':
        mulheres.append(nome)
    idade = input('Idade: ')
    media += idade
    info[cont] = infotemp[:]
    cont += 1
    infotemp.clear()
    confirm = str(input('Quer continuar? ')).upper().strip()[0]
    if confirm in 'N':
        break
    
print(info)
print(f'O grupo tem {cont} pessoas.')

print(f'a média de idade é {media:.0f}')
