from time import sleep
def conta(ini, fim, ps):
    if ps < 0:
        ps = ps * -1
    if ps == 0:
        ps = 1
    print('-='*30)
    print(f'Contagem de {ini} a {fim} de {ps} em {ps}')
    if ini>fim:
        ps = ps * -1
        fim = fim-1
    else:
        fim = fim +1
    for x in range(ini, fim, ps):
        print(f'{x} ',end=' ')
        sleep(0.5)
    print('Fim')



#programa principal
conta(1,10,1)
conta(10,0,2)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
final = int(input('Fim: '))
passo = int(input('Passo: '))

conta(inicio,final,passo)