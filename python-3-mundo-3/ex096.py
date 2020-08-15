def cal(a, b):
    area = a * b
    print(f'A área de um terreno {larg} x {comp} é {area}m²')

    
larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
cal(larg, comp)