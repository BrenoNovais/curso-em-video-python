'''nome = str(input('Digite seu nome completo:')).strip()'''
nome = str('Breno Novais Mota').strip()
print('Seu nome em maiúsculas é:',nome.upper())
print('Seu nome em minúsculas é:{}'.format(nome.lower()))
print('seu nome tem ao todo:', (len(nome) - nome.count(' ')))
print('Seu primeiro nome contem {} letras'.format(nome.find(' ')))

'''nome = str(input('Digite seu nome completo'))
print('Seu nome em maiúsculas é:',nome.upper())
print('Seu nome em minúsculas é:',nome.lower())
dividido = nome.split()
junto = dividido[0] + dividido[1] + dividido[2]
print('Seu nome contem',len(junto),'letras')
pn = dividido[0]
print('Seu primeiro nome contem',len(pn),'letras')'''
