soma = cont = 0
while True:
    num = int(input('Digite numeros: '))
    if num == 999: break
    soma += num
    cont += 1
print(f'Você digitou {cont} números, a somas deles é: {soma}')

