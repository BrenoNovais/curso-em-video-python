ext = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete',\
'Oito', 'Nove', 'Dez', 'Onze', 'Doze','Trêze', 'Quatorze', 'Quinze',\
 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'vinte'
a = True
while a == True:
    num = int(input('Digite um número entre 0 a 20: '))
    if num >=0 and num <= 20:
        print(ext[num])
        while True:
            fim = str(input('Quer continuar?: [S][N]')).upper().strip()
            if fim == 'N':
                a = False
                break
            else:
                break
    else:
        print('Numero invalido!')
print('Programa finalizado')