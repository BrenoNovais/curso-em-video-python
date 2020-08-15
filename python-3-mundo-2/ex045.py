from random import choice
print('{:=^40}'.format(' JoquenPô '))
p1 = str(input('Escolha: Pedra, Papel, ou Tesoura!')).upper().strip()
lista = ['PEDRA', 'PAPEL', 'TESOURA']
p = 'PEDRA'
pp = 'PAPEL'
t = 'TESOURA'
pc = choice(lista)
print('='*40)
if pc == p and p1 == t:
    print('Você perdeu, eu escolhi {}'.format(pc))
elif pc == pp and p1 == p:
    print('Você perdeu, eu escolhi {}'.format(pc))
elif pc == t and p1 == pp:
    print('você perdeu, eu escolhi {}'.format(pc))
elif pc == p1 :
    print('EMPATAMOS, Ambos escolhemos {}'.format(p1))
else:
    print('VOCÊ GANHOU, Eu escolhi {}'. format(pc))
