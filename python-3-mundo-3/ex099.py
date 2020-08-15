from time import sleep
def maior(* lista):
    print('='*30)
    print('Analisando os valores passados...')
    sleep(2)
    for a, b in enumerate(lista):
        print(f'{b} ',end='')
    print(f'Foram informados {len(lista)} valores ao todo.')
    print(f'O maior valor informado foi {max(lista)}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)