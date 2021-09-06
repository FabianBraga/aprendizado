from datetime import date
atual = date.today().year
nasc= int(input('Ano de nascimento: '))
idade = atual-nasc
if idade == 18:
    print('Você te que se alistar imediatamente')
elif idade < 18:
    print('Ainda falta {} anos para o alistamento'.format(18-idade))
    print('Seu alistamento vai ocorren  em {}'.format(atual + (18 - idade)))
else:
    print('Você já deveria ter se alistado há {} anos.'.format(idade-18))
    print('Seu alistamento deria ter sido feito a {} anos.'.format(idade-18))
    print('Seu alistamento foi feito em {}'.format(atual-(idade-18)))