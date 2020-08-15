frase = str(input("Digite uma frase")).strip().upper() #li a frase sem espaços inicio/fim e toda maiúscula.
palavras = frase.split() #criei uma lista com todos os caracteres.
junto = ''.join(palavras) #juntei todos os itens da lista SEM ESPAÇO.
inverso = '' #inverso não recebe nada
for letras in range(len(junto) -1, -1, -1): #for da ultima letra para a primeira contando quantos caracteres tem
    inverso += junto[letras] #inverso recebe o inverso + junto ======= usei para 'somar' as letras do junto
if inverso == junto:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')

print(junto, inverso)
