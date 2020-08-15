while True:
    print('-'*30)
    num = int(input('Quer ver a tabuada de qual valor?'))
    print('-'*30)
    if num < 0: break
    for num2 in range(1, 11):
        print(f'{num} X {num2} = {num * num2}')
print('Tabuada finalizada.')
print('-'*30)