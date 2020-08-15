from time import sleep
print('OS FOGOS VÃO ESTOURAR EM:')
for a in range(10, -1, -1):
    print('{:=^20}'.format(a))
    sleep(1)
print('FELIZ ANO NOVO')