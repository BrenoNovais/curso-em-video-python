def lin(msg):
    print('='*len(msg))
    print(msg)
    print('='*len(msg))


while True:
    lin('\033[0;31;44m SISTEMA DE AJUDA PyHELP')
    func = str(input('\033[0;31;40mDigite o a função para saber como funciona: \33[m'))
    print('\033[0;31;44m')
    print(f'{help(func)}\33[m')