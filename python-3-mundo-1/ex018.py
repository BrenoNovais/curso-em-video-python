from math import radians, cos, tan, sin
ang = float(input('Digite um angulo'))
seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print('O angulo de {}º tem o seno de {:.2f}' .format(ang, seno))
print('o angulo de {}º tem o cosseno de {:.2f}' .format(ang, coss))
print('O angulo de {}º tem a tangente de {:.2f}' .format(ang, tang))
