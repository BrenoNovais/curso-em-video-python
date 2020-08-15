from datetime import date
cad = {}
atual = date.today().year
print('=-='*20)
cad['nome'] = str(input('Digite o nome: '))
cad['idade'] = atual - int(input('Digite a ano de nascimento: ')) 
cad['ctps'] = int(input('Carteira de trabalho: [0] Não tem '))
if cad['ctps'] != 0: 
    cad['contratação'] = int(input('Ano de contratação: '))
    ts = 35 - (atual - cad['contratação'])
    if ts < 0:
        cad['aposentadoria'] = 'Aposentado'
    else:
        cad['aposentadoria'] = cad['idade'] + ts
    cad['salário'] = float(input('Salário: '))
print('=-='*20)
for a, b in cad.items():
    print(f'{a} Tem o valor: {b}')

