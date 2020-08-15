from random import randint
pc = randint(1,10)
acertou = False
palpite = 0
print('VAMOS JOGAR, Vou escolher um numero entre 1 e 10, tente acertar!!')
while not acertou:
    p1 = int(input('Escolha um número:'))
    palpite += 1
    if p1 == pc:
        acertou = True
    else:
        if p1 > pc:
            print('Você errou, tente menos!')
        elif p1 < pc:
            print('Você errou, tente mais!')
print('Parabéns, eu escolhi {} e você {}'.format(pc, p1))
print('Você precisou de {} Tentativas para acertar'.format(palpite))




