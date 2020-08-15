def fatorial(num, show=False):
    """=> Calcula o Fatorial de um número.
:param n: O número a ser calculado.
:param show: (opcional) Mostrar ou não a conta.
:return: o valor fatorial de um número n."""
    f = 1
    for c in range(5, 0, -1):
        if show == True:
            print(f'{c} ' ,end='')
            if c != 1:
                print('x ',end='')
            else:
                print('= ',end='')
        f*= c
    print(f'{f}')

fatorial(5, True)
help(fatorial)
