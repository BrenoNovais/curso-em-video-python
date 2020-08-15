from datetime import date
nasc = int(input('Em que ano você nasceu?'))
idade = date.today().year - nasc
faltam = 18 - idade
atraso = idade - 18

if idade < 18:
    print('Você deve se alistar em {} anos!'.format(faltam))
elif idade == 18:
    print('Você deve se alistar esse ano!')
elif idade > 18:
    print('Você esta atrasado em {} anos!'. format(atraso))

