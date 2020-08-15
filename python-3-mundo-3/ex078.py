valo = []
for pos, val in enumerate(range(0, 5)):
        valo.append(int(input(f'Digite o valor para posição {pos}: ')))
print(f'Valores: {valo}')
print(f'O maior valor digitado foi: {max(valo)} nas posições: ',end='')
for p, v in enumerate(valo):
    if max(valo) == v:
        print(f'{p}...',end='')
print()
print(f'O menor valor digitado foi: {min(valo)} nas posições: ',end='')
for p , v in enumerate(valo):
    if min(valo) == v:
        print(f'{p}...', end='')
print()