def leiaDinheiro(a):
    if a.isnumeric():
        a = a
        return a
            
    else:
        while True:
            print(f'ERRO: {a} é um preço inválido!')
            a = input('Digite o preço: R$')
            if a.isnumeric():
                return a
                break
        