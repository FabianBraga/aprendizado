vel = float(input('Informe a velocidade: '))
if vel > 80:
    print('\033[1;31m Atenção \033[mvocê acaba de receber uma multa por ecesso de velocidade')
    print('aferido \033[1;33m{}\033[m Km/h que vai te custar: R${:.2f}'.format(vel,(vel-80)*7))
