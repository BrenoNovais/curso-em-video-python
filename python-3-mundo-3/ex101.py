def voto(a):
    from datetime import date
    data = date.today().year
    idade = data - a
    if idade > 18 and idade < 65 :
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif idade >= 16 and idade <18 or idade >= 65 :
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: NÃO VOTA.'
    
nasc = int(input('Digite o ano de seu nascimento: '))
print(voto(nasc))



