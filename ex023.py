nm = int(input('Informe um numero inteiro entre 0 e 9999: '))
print('Unidade {} \nDezena {} \nCentena {} \nMihar {}'.format(nm//1 % 10, nm//10 % 10, nm//100 % 10, nm//1000 % 10))