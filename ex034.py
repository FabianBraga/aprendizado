sl = float(input('Informe o salário a calcular: '))
if sl >1250:
    print('O seu novo salário é de R$ {:.2f} com um reajuste de 10%'.format(sl*1.1))
else:
    print('O seu novo salário é de R$ {:.2f} com um reajuste de 15%'.format(sl * 1.15))