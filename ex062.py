tm = int(input('Informe o primeiro termo: '))
rz = int(input('Informe a razão: '))
ct = 10
while ct>0:
    ct-=1
    print(tm,end='')
    if ct != 0:
        print('-',end='')
    if ct == 0:
        print('')
        ct = int(input('Você gostaria de mostrar mais quantos termos? digite [ 0 ] para encerrar: '))
    tm+=rz
