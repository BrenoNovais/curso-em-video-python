sal = float(input('Qual seu salario'))
if sal <= 1250:
    sal2 = sal * 1.15
else:
    sal2 = sal * 1.10
print('Seu salário com aumento é:R${:.2f}'.format(sal2))