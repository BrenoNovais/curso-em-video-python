num = 0
num2 = 0
end = 0
cont = 0
while end < 1:
    num = int(input('Digite um numero, ou [999] para parar: '))
    if num != 999:
        num2 += num
        cont += 1
    else:
        end += 1
print('Foram digitados {} números e a soma deles é: {}'.format(cont, num2))