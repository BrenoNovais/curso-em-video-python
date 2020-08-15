from random import randint
print('-'*30)
print('Vamos jogar par ou impar!')
print('-'*30)
pcnum = soma = cont = 0
poi = ''
poie = ''
while True:
    pcnum = randint(1, 10)
    playernum = int(input('Diga um valor: '))
    soma = playernum + pcnum
    escolhi = str(input('Par ou ímpar? [P][I]')).upper().strip()[0]
    if soma % 2 == 0:
        poi += 'PAR'
        poie += 'P'
        if escolhi not in poie:
            break
    elif soma % 2 != 0:
        poi += 'IMPÁR'
        poie += 'I'
        if escolhi not in poie:
            break
    print(f'Eu escolhi: {pcnum} e você: {playernum} a soma é {soma}, {poi}.')
    print('Você ganhou, vamos novamente!')
    poi = ''
    poie = ''
    cont += 1
print(F'você escolheu {poi} e número {playernum}, a maquina escolheu {pcnum}, a soma é: {soma}, {poi}.')
print(f'Game over, você ganhou {cont} vezes!!')
