tabela = 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia', 'Botafogo', 'Bragantino', 'Ceará', 'Corinthians', 'Coritiba',\
         'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacional',\
         'Palmeiras', 'Santos', 'São Paulo', 'Sport', 'Vasco'
print(f'Lista de times do brasileirão:\n{tabela}')
print('='*220)
print(f'Os 5 primeiros são: \n{tabela[0:5]}')
print('='*87)
print(f'Os 4 ultimos são: \n{tabela[-4:]}')
print('='*59)
print(f'Times em ordem alfabética: \n{sorted(tabela)}')
print('='*220)
quem = int(input('Digite posição para consultar: '))
print(f'O time do {tabela[quem - 1]} esta na {quem}ª posição.')

