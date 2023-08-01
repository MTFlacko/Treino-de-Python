import math
an = float(input('Digite o angulo que vc deseja: '))
seno = math.sin(math.radians(an))
print('O angulo de {} tem o seno de {:.2f}'.format(an, seno))
cosseno = math.cos(math.radians(an))
print('O angulo de {} tem o cosseno de {:.2f}'.format(an, cosseno))
tangente = math.tan(math.radians(an))
print('O angulo de {} tem a tanfente de {:.2f}'.format(an, tangente))
