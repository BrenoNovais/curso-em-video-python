from datetime import date
ano = int(input('Qual ano de nascimento do atleta?'))
id = date.today().year - ano
if id <= 9:
    print('Este é um atleta Mirim!')
elif id >= 14 and id < 19:
    print('Este é um atleta Infantil!')
elif id > 14 and id <= 20:
    print('este é um atleta Sênior!')
elif id > 20:
    print('Este é um atleta Master')
print(id)