peso = float(input('Qual seu peso?'))
altura = float(input('Qual sua altura?'))
imc = peso / (altura ** 2)
print('Seu peso esta na faixa de:', end=' ')
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso ideal')
elif imc > 25 and imc <= 30:
    print('Sobrepeso')
elif imc > 30 and imc <= 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade mórbida')
print(float(imc))