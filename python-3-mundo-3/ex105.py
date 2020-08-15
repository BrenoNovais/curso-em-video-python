def notas(*notas, sit):
    nts = 0
    temp = {}
    for a, b in enumerate(notas):
        nts += b
    media = nts / len(notas)
    temp['Total'] = len(notas)
    temp['Maior'] = max(notas)
    temp['Menor'] = min(notas)
    temp['Média'] = media
    if sit == True:
        if media >= 7:
            temp['Situação'] = 'Boa'
        elif 7 > media > 6:
            temp['Situação'] = 'Razoavel'
        else:
            temp['Situação'] = 'Ruim'
    return temp

        
resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True )
print(resp)