via = float(input('Qual a distância da sua viagem: '))
if via <=200:
    print('Sua viagem tem um custo de R$ 0,50 por Km rodado e vai custar: R$ {}'.format(via*0.5))
else:
    print('Sua viagem tem um custo de R$ 0,45 por Km rodado e vai custar: R$ {}'.format(via * 0.45))