item=0
while item != 5:
    if item == 0:
        nm1 = float(input('Informe o 1º numero: '))
        nm2 = float(input('Informe o 2º numero: '))
    item=int(input('''Menu
    [ 1 ] soma
    [ 2 ] Multiplicação
    [ 3 ] maoir
    [ 4 ] novos números
    [ 5 ] sair do programa
    
    Informe sua opção: '''))
    if item == 1:
        res = nm1 + nm2
    elif item == 2:
        res = nm1 * nm2
    elif item == 3:
        res = max(nm1,nm2)
    elif item == 4:
        item = 0
    else:
        print('Obrigado por utilizar o nosso serviço. Volte sempre...')
    if item != 5 and item != 0:
        print('O resultado é: \033[33m{}\033[m'.format(res))