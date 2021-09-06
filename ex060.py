nm = int(input('Informe o numero: '))
ct = nm + 1
nm2 = 1
print('O fatorial de \033[31m{}\033[m é: '.format(nm), end='')
while ct != 1:
    ct-=1
    if ct>1:
        print('{} x '.format(ct), end=' ')
        nm2 *= ct
    else:
        print(ct,' = ', end='')
print('\033[31m{}\033[m'.format(nm2))