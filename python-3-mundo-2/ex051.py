pt = int(input('Digite o PRIMEIRO TERMO: '))
rz = int(input('Digite a RAZÃO: '))
rt = pt + (10 * rz)
print('Os 10 primeiros termos da P.A com Primeiro termo {} e Razão {} são: '.format(pt, rz))
for a in range(pt, rt, rz):
    print('{}'.format(a), end=' ')