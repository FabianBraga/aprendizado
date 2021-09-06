th = td = tm = an = 0
while True:
    sx = sn = ' '
    print('-' * 50)
    print('cadastre uma pessoa'.upper())
    print('-' * 50)
    an = int(input('Idade: '))
    while sx not in 'MF':
        sx = input('Sexo [M/F]: ').strip().upper()[0]
    if sx in 'M':
        th += 1
    if an > 18:
        td += 1
    if sx in 'F' and an < 20:
        tm +=1
    while sn not in 'SsNn':
        sn = input('Quer continuar [S/N]: ').upper().strip()[0]
    if sn in 'N':
        break
print(f'{ "FIM DO PROGRAMA":=^50}')
print(f'Total de pessoas com mais de 18 anos: {td}')
print(f'Total de Homems cadastrados: {th}')
print(f'Total de Mulheres com menos de 20 anos: {tm}')

