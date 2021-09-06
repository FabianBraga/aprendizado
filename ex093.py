jogador = {}
gols = []
jogador['nome'] = input('Nome do dados: ')
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for x in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {x}: ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-='*30)
print(jogador)
print('-='*30)
for c, n in jogador.items():
    print(f'O campo {c} tem o valor {n}')
print('-='*30)
print(f'O dados {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
ct = 0
for x in jogador['gols']:
    print(' '*5,f'Na partida {ct}, fez {x} gols.')
    ct += 1
