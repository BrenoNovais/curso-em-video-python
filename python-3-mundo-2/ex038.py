num1 = int(input('Digite um valor'))
num2 = int(input('Digite outro valor'))
if num1 > num2:
    print('O primeiro valor {} é maior.'.format(num1))
elif num2 > num1:
    print('O segundo valor {} é maior'.format(num2))
elif num1 == num2:
    print('Não exite valor maior, {} e {} são iguais'.format(num1, num2))