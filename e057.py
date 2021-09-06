sx=''
while True:
    sx = str(input('digite o sexo [M/F]: ')).strip().upper()
    if sx != 'M' and sx != 'F':
        print('A resposta só dopde ser M ou F, tente novamente')
    else:
        exit()