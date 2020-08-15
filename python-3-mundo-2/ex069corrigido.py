tot18 = totm = totalm20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).upper().strip()[0]
    if idade < 18:
        tot18 += 1
    if sexo == 'M':
        totm += 1
    if sexo == 'F' and idade < 20:
        totm += 1
    resp = ' '
    while resp not in 'SN':
            resp = str(input('Quer continuar? [S][N]')).upper().strip()[0]
    if resp == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos {tot18}
Homens cadastrados {totm}
Mulheres com menos de 20 anos {totalm20}
''')