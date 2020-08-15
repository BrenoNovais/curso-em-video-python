palavras = 'aprender', 'programar', 'linguagem', 'python', 'curso',\
'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',\
'programador', 'futuro', 'aaaaaa'
vogais = ''
v = 'a', 'e', 'i', 'o', 'u'
for palavra in palavras:
    cont = 0
    z = list(palavra)
    while len(z) > cont:
        if z[cont] in v:
            vogais += z[cont]
        cont += 1
    print(f'Na palavra {palavra} temos: {vogais} ')
    vogais = ''
