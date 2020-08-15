def metade(n=0, mone=False):
    ''' 
    -> Calcula o aumeto de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param n: o preço que se quer reajustar
    :param p: qual a porcentagem do aumento.
    :param mone: quer a saida monetaria ou não?
    :return: o valor reajustado, com ou sem formato
    '''
    res = n / 2
    return res if mone is False else moeda(res)
        

def dobro(n=0, mone=False):
    res = n + n 
    return res if not mone else moeda(res)
    


def aumentar(n=0, p=0, mone=False):
    res = n + (n * p/100)
    return res if not mone else moeda(res)
    ''' 
    -> Calcula o aumeto de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param n: o preço que se quer reajustar
    :param p: qual a porcentagem do aumento.
    :param mone: quer a saida monetaria ou não?
    :return: o valor reajustado, com ou sem formato
    '''

def diminuir(n=0, p=0, mone=False):
    res = n - (n * p/100)
    return res if not mone else moeda(res)


def moeda(n):
    n = str(f'R${n:.2f}').replace('.', ',')
    return n


def resumo(n1=0, n2=0, n3=0):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'{"Preço analisado:"} \t{moeda(n1)}')
    print(f'{"Dobro do preço:"} \t{dobro(n1, True)}')
    print(f'{"Metade do preço:"} \t{metade(n1, True)}')
    print(f'{n2} {"% de aumento"} \t{aumentar(n1, n2, True)}')
    print(f'{n3} {"% de redução"} \t{diminuir(n1, n3, True)}')
    print('-'*30)
