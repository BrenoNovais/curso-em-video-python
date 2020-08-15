dicionario = {}
dicionario['Nome'] = str(input('Nome: '))
dicionario['Média'] = float(input(f'Média: '))
if dicionario['Média'] >= 7:
    dicionario['Situação'] = 'Aprovado'
elif 5 <= dicionario['Média'] < 7:
    dicionario['Média'] = 'Recuperação'
else:
    dicionario['Situação'] = 'Reprovado'
for chave, valor in dicionario.items():
    print(f'{chave} é: {valor}')