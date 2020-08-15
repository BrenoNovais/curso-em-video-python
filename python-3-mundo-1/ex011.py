a = (float(input('Qual a altura da parede?')))
l = (float(input('Qual a largura da parede?')))
ar = a*l
t = (0.5)
qt = t*ar
print('A Area da sua parede é {}m². serão necessarios {:.1f} litros de tinta' .format(ar, qt))