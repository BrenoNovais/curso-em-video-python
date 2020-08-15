print('='*20)
print('CADASTRE UMA PESSOA')
print('='*20)
conti = conds = contf = contm = 0
while True:
    idade = int(input('Digite a IDADE:'))
    if idade > 18:
        conti += 1
    while True:
        sexo = str(input("Digite o SEXO: [M][F] ")).upper().strip()[0]
        if sexo not in 'F, M':
            print(f'{sexo}Sexo invalido!')
        else:
            if sexo in 'F' and idade < 20:
                contf += 1
            elif sexo in 'M':
                contm += 1
        break
    print('='*24)
    new = str(input('Quer continuar? [S][N]')).upper().strip()[0]
    print('='*24)
    if new in 'N':
        break
print('='*33)
print('FIM DO PROGRAMA')
print(f'Maiores de idade: {conti}')
print(f'Homens cadastrados: {contm}')
print(f'Mulheres com menos de 20 anos: {contf}')
print('='*33)