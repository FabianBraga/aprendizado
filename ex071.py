print('='*50)
print(f'{ "BANCO FERRADURA":^50}')
print('='*50)
vl = int(input('qual o valor deseja sacar: R$ '))
print('-'*50)
if vl>=50:
    print(f'Total de {vl//50} cedulas de R$ 50,00')
    vl = vl - (vl//50*50)
if vl>=20:
    print(f'Total de {vl//20} cedulas de R$ 20,00')
    vl = vl - (vl//20*20)
if vl>=10:
    print(f'Total de {vl//10} cedulas de R$ 10,00')
    vl = vl - (vl//10*10)
if vl>=1:
    print(f'Total de {vl} cedulas de R$ 1,00')
print('='*50)
print(f'{ "VOLTE SEMPRE AO BANCO FERRADURA":^50}')