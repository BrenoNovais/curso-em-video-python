a = float(input('Digite o comprimento da reta A'))
b = float(input('Digite o comprimento da reta B'))
c = float(input('Digite o comprimento da reta C'))
if a + b > c and a + c > b and b + c > a:
    print('Os comprimentos {} + {} + {} podem formar um triângulo'.format(a, b, c))
else:
    print('Os comprimentos {} + {} + {} não podem formar um triângulo'.format(a, b, c))

