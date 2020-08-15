sexo = ''
pedido = 'F, f, M, m'
while sexo != pedido:
    sexo = str(input('Digite seu sexo:\nMASCULINO[M]\nFEMININO [F]')).strip().upper()[0]
    if sexo in 'fFMm':
        sexo = pedido
    elif sexo != pedido:
        print('SEXO INVALIDO!!')
print('SEXO ACEITO,{}')


