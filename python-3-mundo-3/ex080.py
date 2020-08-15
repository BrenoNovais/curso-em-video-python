fixa = []
for a in range(0, 5):
    num = int(input(f'Digite o {a + 1}º número:'))
    print('O valor foi adicionado ',end='')
    if len(fixa) == 0:
        fixa.insert(0, num)
        print('na unica posição possivel fdp ele é o primeiro')
    elif len(fixa) == 1:
        if num < fixa[0]:
            fixa.insert(0, num)
            print(f'Na posição {fixa.index(num)}')
        if num > fixa[0]:
            fixa.insert(1, num)
            print(f'Na posição {fixa.index(num)}')
    else:
        for b in range(0, len(fixa)):
            if num > fixa[b] and num < fixa[b + 1]:
                fixa.insert(b + 1, num)
                print(f'Na posição {fixa.index(num)}')
                break
            if num > max(fixa):
                fixa.append(num)
                print(f'Na posição {fixa.index(num)}')
                break
            if num < min(fixa):
                fixa.insert(0, num)
                print(f'Na posição {fixa.index(num)}')
                break
        print(fixa)
        b = 0
            