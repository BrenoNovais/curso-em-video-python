cont = 0
imp = 0
for a in range(1, 501, 2):
    if a % 3 == 0:
        cont += +1
        imp += a
print('A soma dos {} numeros IMPARES entre 1 e 500 é: {}' .format(cont, imp))
