print('='*30)
print('        BANCO PHYTON')
print('='*30)
valor = int(input('Quanto quer sacar?: R$'))
notas50 = valor // 50
sobra50 = valor - (notas50 * 50)
notas20 = sobra50 // 20
sobra20 = sobra50 - (notas20 * 20)
notas10 = sobra20 // 10
sobra10 = sobra20 - (notas10 * 10)
notas1 = sobra10 // 1
print(f'{notas50} Notas de R$50')
print(f'dinheiro restante{sobra50}')
print(f'{notas20} Notas de R$20')
print(f'dinheiro restante{sobra20}')
print(f'{notas10} Notas de R$10')
print(f'dinheiro restante{sobra10}')
print(f'{notas1} Notas de R$1')
