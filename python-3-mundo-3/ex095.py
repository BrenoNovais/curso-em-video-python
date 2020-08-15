jogador = {}
gols = []
partidas = contg = 0
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    for a in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {a+1}?')))
    jogador['gols'] = gols.copy()
    for b, c in enumerate(gols):
        contg += c
    jogador['total'] = contg
       print('=-'*20)
    print(jogador)
print('=-'*20)
for d, e in jogador.items():
    print(f'O campo {d} tem o valor {e}')
print('=-'*20)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for f in range(0, partidas):
    print(f'   => Na partida {f + 1}, fez {jogador["gols"][f]} gols')
print(f'Foi um total de {jogador["total"]} gols.')