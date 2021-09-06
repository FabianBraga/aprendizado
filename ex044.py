vl = float(input('Valor das compras: \033[;31mR$\033[m '))
fp = int(input('''FORMA  DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x no cartão
Quala opção desejada: '''))
vf = 0
pc = 1
if 0 < fp > 4:
    print('Forma de pagamento não cadastrada')
elif fp == 1:
    vf = vl * 0.9
elif fp == 2:
    vf = vl * 0.95
elif fp == 3:
    vf = vl
    pc = 2
elif fp == 4:
    vf = vl * 1.2
    pc = 3
if pc == 1:
    print('O valor devido é de R$ {:.2f} '.format(vf))
else:
    print('O valor devido é de R$ {:.2f} e a sua parcela é de R$ {:.2f}'.format(vf, vf/pc))
