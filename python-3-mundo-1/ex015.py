km = float(input('Quantos quilometros foram percorridos?'))
dias = float(input('Quantos dias ele ficou alugado?'))
total = km * 0.15 + dias * 60
print('O total a pagar é de {:.2f}R$' .format(total))