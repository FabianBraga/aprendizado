n1 = int(input('Informe o 1º numero: '))
n2 = int(input('Informe o 2º numero: '))
n3 = int(input('Informe o 3º numero: '))
if n1>n2:
    if n1>n3:
        print('O primeiro numero digitado {} é o maior da cadastro'.format(n1))
    else:
        print('O terceiro numero digitado {} é o maior da cadastro'.format(n3))
else:
    if n2>n3:
        print('O segundo numero digitado {} é o maior da cadastro'.format(n2))
    else:
        print('O terceiro numero digitado {} é o maior da cadastro'.format(n3))