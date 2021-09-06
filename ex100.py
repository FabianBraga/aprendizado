from random import randint
from time import sleep


def sorteio(qt):
    retorno = []
    print(f'Sorteando {qt} valores da lista: ',end='')
    for x in range(0,qt):
        retorno.append(randint(1, 10))
        print(retorno[x], end=' ')
        sleep(0.5)
    print('Pronto!')
    return retorno

def somapar(item):
    soma = 0
    for x in item:
        if x % 2 == 0:
            soma += x
    print(f'Somando os valores pares de {item}, temos {soma}')
    return soma


# programa principal
somapar(sorteio(4))

