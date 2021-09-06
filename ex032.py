ano = int(input('Informe o ano: '))
if ano%4==0:
    print('O ano {} é um ano bissexto.'.format(ano))
else:
    print('O ano {} não é Bissexto.'.format(ano))