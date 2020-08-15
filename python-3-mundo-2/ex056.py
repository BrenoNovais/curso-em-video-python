somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totalm = 0
for lista in range(1, 5):
    nome = str(input('Digite seu nome:')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input("Digite seu sexo: (H/M) ")).strip()
    somaidade += idade
    if lista == 1 and sexo == 'Hh':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Hh' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if  sexo in 'mM' and idade < 20:
        totalm += 1

mediaidade = somaidade / 4
print('A media de idade do grupo é: {}'.format(mediaidade))
print('O nome do homem mais velho é: {}, com {} anos.'.format(nomevelho, maioridadehomem))
print('No grupo contem {} mulheres com menos de 20 anos.'.format(totalm))


