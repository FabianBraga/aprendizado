dolar=float(input('Informe a cotação do dólar para a conversão: '))
real= float(input('Informe o valor que quer converter: R$'))
print('Com R${:.2f} e possível comprar U${:.2f}'.format(real,real/dolar))