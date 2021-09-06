from time import sleep
def maior(*par):
    print('-='*30)
    print('Analisando os valores passados...')
    if len(par) == 0:
        print('foram informados 0 valores')
        print('O maior valor informado foi 0')
        exit()
    for x in par:
        print(x,end=' ')
        sleep(0.5)
    print(f'Foram informados {len(par)} valores ao todo.')
    print(f'O maior valor informado foi {max(par)}.')


#Programa principal

maior(1,2,7,8,2,5,6)
maior(1,0,2)