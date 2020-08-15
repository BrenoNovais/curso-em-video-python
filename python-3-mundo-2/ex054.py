from datetime import date
atual = date.today().year
al = 0
nal = 0
for na in range(1, 8):
    todas = int(input('Qual a data de nasciment? '))
    idade = atual - todas
    if idade >= 21:
        al += 1
    else:
        nal += 1
print('{} Pessoas ja alistaram'.format(al))
print('{} Pessoas não alistaram'.format(nal))