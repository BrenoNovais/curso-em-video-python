lista1 = []
lista2 = []
exp = input('Digite uma expressão: ')
if exp.count('(') == exp.count(')'):
    print('Sua expressão é correta!')
else:
    print('Sua expressão não é valida!')