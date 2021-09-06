from random import randint
from time import sleep
lista=[]
print('-'*40)
print(F'{"JOGA NA MEGA SENA":^40}')
print('-'*40)
qt = int(input('Quantos jogos você quer que eu sortei? '))
for x in range(qt):
    num = []
    item = ct = 0
    while ct < 7:
        item = randint(1, 60)
        if item not in num:
            num.append(item)
            ct+= 1
    num.sort()
    lista.append(num[:])
print('-='*10,f'SORTEANDO {qt} JOGOS','-='*10)
for x in range(qt):
    print(f'Joga {x+1}: ',lista[x])
    sleep(1)
print(f'{" BOA SORTE ":=^40}')
