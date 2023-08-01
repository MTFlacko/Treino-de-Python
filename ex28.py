from random import randint
computador = randint(0, 5) #faz pensar
print('-=-'* 20)
print('Vou pensar em um numero de 0 a 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em qual numero eu pensei '))
if jogador == computador:
    print('Parabéns você conseguiu me vencer')
else:
    print('Ganhei eu pensei no numero {} e não no {}'.format(computador, jogador))