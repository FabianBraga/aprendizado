ca = float(input('Qual o valor pretendido para o financiamento: '))
sa = float(input('Quanto você recebe de salário: '))
tp = int(input('Em quantos anos pretende pagar o financiamento: '))
ap = ca/(tp*12)
if sa*30/100<ap:
    print('Financiamento \033[;31m reprovado\033[m!\nsua parcela foi de R${:.2f} e a sua capacidade de individamento é de R${:.2f}'.format(ap,sa*30/100))
else:
    print('Financiamento \033[;33m Aprovado\033[m!\nSuas parcelas vão ser de R$ {:.2f}'.format(ap))