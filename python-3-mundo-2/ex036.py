valorc = float(input('Qual valor da casa?'))
salario = float(input('Qual seu sálario?'))
tempo = int(input('Em quantos anos pretende pagar?'))
meses = tempo * 12
mensal = valorc / meses
if salario * 0.3 >= mensal:
    print('Parabéns, seu empréstimo foi \033[0;30;44maprovado.\033[m')
    print('Serão discontadas {:.0f} Parcelas de R${:.2f} mensais'.format(meses, mensal))
else:
    print('Seu empréstimo foi \33[0;30;41mnegado\33[m.')

