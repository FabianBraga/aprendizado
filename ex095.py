dados = {}
lista = []
while True:
    gols = []
    dados['nome'] = input('Nome do dados: ')
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    tot = 0
    for x in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {x}: ')))
        tot += int(gols[x])
    dados['gols'] = gols[:]
    dados['total'] = sum(gols)
    lista.append(dados.copy())
    while True:
        sn = input('Quer continuar [S/N]: ').upper()[0]
        if sn in 'SN':
            break
    if sn == 'N':
        break
print('-'*45)
print('Cod ',end='')
for x in dados.keys():
    print(f'{x:<15}',end='')
print()
print('-'*45)
for x, y in enumerate(lista):
    print(f'{x:>3} ',end='')
    for d in y.values():
        print(f'{str(d):<15}',end='')
    print()
print('<> ' * 30)
while True:
    varre = int(input('Mostrar dados de qual dados (999 encerra): '))
    if varre == 999:
        break
    if varre > len(lista)-1:
        print(f'ERRO! Não existe dados com o código {varre}! tente novamente')
    else:
        print('<> '*30)
        print(f'--- LEVANTAMENTO DO JOGADOR {lista[varre]["nome"]}:')
        for x, y in enumerate(lista[varre]['gols']):
            print(' '*5,f'Na partida {x+1}, fez {y} gols.')
        print('<> '*30)
print('< <VOLTE SEMPRE> >')
