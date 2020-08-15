print('='*30)
print('         LOJÃO PYTHON')
print('='*30)
total = mm = mb = conta = 0
nmb = ''
while True:
    nome = str(input('Nome do Produto: '))
    price = float(input('Preço do Produto: R$'))
    conta += 1
    total += price
    if price >= 1000:
        mm += 1
    if conta == 1 or price < mb:
        mb = price
        nmb = nome
    print('=' * 30)
    while True:
        cont = str(input('Quer Continuar? [S][N]')).upper().strip()[0]
        if cont in 'S' or cont in 'N':
            break
    print('=' * 30)
    if cont in 'N':
        break
print('='*30)
print(f'o preço da compra é de: R${total}')
print(f'{mm} Produtos custam mais de R$1000')
print(f'O produto mais barato é: {nmb} custando, R${mb}')

