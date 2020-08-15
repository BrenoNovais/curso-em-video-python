preço = float(input('Qual preço do produto'))
#desconto = preço/100*95
desconto = preço - (preço * 5 / 100)
print('O preço com desconto é de R${:.2f}' .format(desconto))
