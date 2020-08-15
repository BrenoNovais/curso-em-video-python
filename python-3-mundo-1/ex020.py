from random import sample
aluno1 = str(input('Primeiro aluno'))
aluno2 = str(input('Segundo aluno'))
aluno3 = str(input('Quarto aluno'))
aluno4 = str(input('Quarto aluno'))
lista = [aluno1, aluno2, aluno3, aluno4]
sequencia = sample(lista, 4)
print('A ordem de apresentação sera: {}' .format(sequencia))

