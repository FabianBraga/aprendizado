def fator(num,show=False):
    """->Calcula o fatorial de um número.
    onde num: O numero a ser calculado.
    onde show: (opcional Mostra ou não o calculo.
    Retorna o valor fatorial de num"""

    cal = 1
    for x in range(num,0,-1):
        cal*=x
        if show:
            print(f'{x}',end='')
        if show and x !=1:
            print(' X ', end='')
        if show and x == 1:
            print(' = ', end='')
    return cal


#Programa principal
print(fator(5,True))
print(fator(3,True))
help(fator)