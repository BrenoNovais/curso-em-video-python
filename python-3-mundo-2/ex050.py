soma = 0
quant = 0
for a in range(6):
    b = int(input('Digite um numero: '))
    if b % 2 == 0:
     soma += b
     quant += +1
print('A soma dos {} valores pares digitados é: {}'.format(quant, soma))