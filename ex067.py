while True:
    tb = int(input('Quer ver a tabuada que qual valor?  '))
    if tb < 0:
        break
    op = str(input('''[ 1 ] Multiplicar [ 2 ] Dividir [ 3 ] Somar [ 4 ] Subitrair 
       Qual a operação? '''))
    print('-'*50)
    x = 0
    if op in '1234':
        for x in range(1,11):
            if op == '1':
                print(f'{tb} x {x} = {x * tb}')
            elif op == '2':
                if tb != 1:
                    print(f'{x * 10} ÷ {tb} = {x}')
                else:
                    print(f'{x} ÷ {tb} = {x}')
            elif op == '3':
                print(f'{tb} + {x} = {x + tb}')
            elif op == '4':
                print(f'{tb} - {x} = {tb - x}')
    else:
        print('opção inválida tente novamente!!!')

