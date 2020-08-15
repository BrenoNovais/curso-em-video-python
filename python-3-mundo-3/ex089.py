nome = ''
nota = cont = 0
nota2 =[]
alunos = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input(f'Nota 1: '))
    nota2 = float(input(f'Nota 2: '))
    media = (nota1 + nota2) / 2      
    alunos.append([nome,[nota1, nota2], media])
    cont += 1
    resp = str(input('Quer continuar? [S][N]')).upper().split()[0]
    if resp in 'N':
        break
print('=-='*25)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for a, b in enumerate(alunos):
    print(f'{a:<4} {b[0]:<10} {b[2]:>8.1f}')
print('-'*30)
while True:
    sep = int(input('Mostrar notas de qual aluno?: [999]Para parar'))
    if sep <= len(alunos) - 1:
        print(f'Notas de {alunos[sep][0]} são: {alunos[sep][1]}')
