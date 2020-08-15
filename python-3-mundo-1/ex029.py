vel = int(input('Qual velocidade do carro?'))
if vel >= 81:
    multa = (vel - 80) * 7
    print('você sera multado em R${:.2f}'.format(multa))
else:
    print('você esta dentro da velocidade limite.')