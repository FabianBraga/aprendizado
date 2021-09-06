from operator import itemgetter
from random import randint
from time import sleep

jogos = {'jogador1':randint(1,6),
         'jogador2':randint(1,6),
         'jogador3':randint(1,6),
         'jogador4':randint(1,6)}
rank = list()
for x, y in jogos.items():
    print(f'O jogador {x} tirou {y} nos dados.')
    sleep(1)
rank = sorted(jogos.items(),key=itemgetter(1),reverse=True)
print('-='*40)
print('===RANKING DOS JOGADORES===')
ct = 1
for x, y in enumerate(rank):
    print(f'{x+1}º Lugar {y[0]} com {y[1]}.')
print(rank)