velo = float(input('Qual é a velocidade do carro? '))
if velo > 80:
    print('MULTADO! você ultrapassou o limite permitido de 80Km')
    multa = (velo-80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Você está no limite permitido')


