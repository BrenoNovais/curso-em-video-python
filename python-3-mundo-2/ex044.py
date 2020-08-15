print('{:=^40}'.format(' LOJAS BRENO '))
valor = float(input('Qual valor da compra?'))
m1 = 'Dinheiro ou cheque'
fp = int(input('''Para pagar com:
Dinheiro ou cheque digite:----[1]
Cartão a vista digite: -------[2]
2x No cartão digite: ---------[3]
3x Ou mais no cartão digite:--[4]
------------------------------ '''))
desconto = 'O valor da sua compra com desconto sera de:'
juros = 'O valor da sua compra com juros sera de:'
if fp == 1:
    print(desconto,'R${:.2f}'.format(valor * 0.90))
elif fp == 2:
    print(desconto,'R${:.2f}'.format(valor * 0.90))
elif fp == 3:
    print('O valor da sua compra sera de: R${:.2f}'.format(valor))
elif fp == 4:
    print(juros,'R${:.2f}'.format(valor * 1.20))
