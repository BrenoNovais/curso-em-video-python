nota1 = float(input('Qual foi sua primeira nota?'))
nota2 = float(input('Qual foi sua segunda nota?'))
nota3 = float(input('Qual foi sua terceira nota?'))
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print('A sua média foi {:.2f} você foi Aprovado!'.format(media))
elif media == 5:
    print('A sua média foi {:.2f} você esta de Recuperação!'.format(media))
elif media < 5:
    print('A sua média foi {:.2f} você esta Reprovado!'.format(media))
