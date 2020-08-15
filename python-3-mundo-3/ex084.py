reg = []
temp = []
mai = men = 0
while True:
    temp.append(str(input('Digite o nome: ')))
    temp.append(int(input('Digite o peso: ')))
    if len(reg) < 2:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
           mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    reg.append(temp[:])
    temp.clear()
    end = str(input('Quer continuar?: [S][N]')).upper().strip()[0]
    if end in 'N':
        break
print(reg)
print(f'Ao todo você cadastrou {len(reg)}')
print(f'O maior peso foi de {mai}Kg. Peso de ',end='')
for a in reg:
    if a[1] == mai:
        print(f'{a[0]}...')
print(f'O menor peso foi de {men}Kg. Peso de ',end='')
for a in reg:
    if a[1] == men:
        print(f'{a[0]}...')



