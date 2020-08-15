a = float(input('Digite o comprimento de A'))
b = float(input('Digite o comprimento de B'))
c = float(input('Digite o comprimento de C'))
if a + b > c and a + c > b and b + c > a:
    print('Os segmentos acima PODEM FORMAR um triângulo', end=' ')
    if a == b and b == c:
        print('Equilatero!')
    elif a == b and b != c or a != b and b == c:
        print('Isósceles!')
    elif a != b and b != c and c != a:
        print('Escaleno!')
else:
    print('Os segmentos {:.0f}, {:.0f} e {:.0f}, Não podem formar um triangulo!'.format(a, b, c))
