num = int(input('Qual a distancia da sua viagem em Km?'))
if num <= 200:
    price = num * 0.50
else:
    price = num * 0.45
print('O preço da sua passagem é de R${:.2f}'.format(price))

