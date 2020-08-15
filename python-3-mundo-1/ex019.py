from random import choice
aluno1 = str(input('Qual nome do aluno?'))
aluno2 = str(input('Qual nome do aluno?'))
aluno3 = str(input('Qual nome do aluno?'))
aluno4 = str(input('Qual nome do aluno?'))
lista = [aluno1, aluno2, aluno3, aluno4]
sorteado = choice(lista)
print('Quem apagara o quadro sera o aluno {}' .format(sorteado))