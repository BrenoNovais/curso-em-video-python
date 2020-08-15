def leiaInt(a):
    valor = 1
    while True:
        try:        
            resp = int(input(a))
        except (ValueError, TypeError):
            print('\033[0;31;40m Erro: por favor, digite um número inteiro válido.\33[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31;40m O usuario preferiu não digitar esse número.\33[m')
            return 0
        else:
            return resp
                
            
def leiaFloat(a):
    while True:
        try:
            resp = float(input(a))
        except (ValueError, TypeError):
            print('\033[0;31;40m Erro: por favor, digite um número real válido.\33[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31;40m O usuario preferiu não digitar esse número.\33[m')
            return 0
        else:
            return resp
           

n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real: ')

print(f'O valor inteiro digitado foi: {n1}')
print(f'O valor real digitado foi: {n2}')
