def ficha(a='', b=0):
    if a == '':
        a = '<Desconhecido>'
    if b == '':
        b = 0
    print(f'O jogador {a} fez {b} gols no campeonato.')

print('='*20)
nome = str(input('Nome do jogador: '))
gols = input('Número de gols: ')
ficha(nome, gols)