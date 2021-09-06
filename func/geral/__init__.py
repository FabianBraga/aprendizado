def metade(v,fo = False):
    """
    ->Divide um valor passado pela sua metade
    :param v: valor a ser calculado
    :return: retorna o valor dividido por 2
    """
    ret = v/2
    return ret if not fo else moeda(ret)


def dobro(v,fo = False):
    """
    ->Dobra um valor passado
    :param v: valor a ser calculado
    :return: retorna o valor dobrado
    """
    ret = v*2
    return ret if not fo else moeda(ret)


def diminuir(v,p=10,fo = False):
    """
    -> Diminui um valor em uma percentagem
    :param v: Valor a ser reduzido
    :param p: porcentagem de correção
    :return: retorna o valor com a correção
    """
    ret = v-(v*p/100)

    return ret if not fo else moeda(ret)


def aumentar(v,p=10,fo = False):
    """
    -> Aumenta um valor em uma percentagem
    :param v: Valor a ser aumentado
    :param p: porcentagem de correção
    :return: retorna o valor com a correção
    """
    ret = v+(v*p/100)
    return ret if not fo else moeda(ret)


def moeda(v,m='R$'):
    ret = f'{m} {v:.2f}'.replace('.',',')
    return ret


def resumo(v,a,d):
    """
    -> Faz um resumo dos calculos
    :param v:
    :param a:
    :param d:
    :return:
    """
    from func import titulo,cor
    titulo('-','RESUMO DO VALOR',50,1,8)
    print(cor(1,7),end='')
    texto = f'{a}% de acrescimo'
    print(f'{"Preço analisado":<20}{moeda(v):>15}')
    print(f'{"Dobro do preço":<20}{dobro(v,True):>15}')
    print(f'{"Metade do preço":<20}{metade(v,True):>15}')
    print(f'{texto:<20}{aumentar(v,a,True):>15}')
    texto = f'{d}% de de redução'
    print(f'{texto:<20}{diminuir(v,d,True):>15}')
    titulo('-', tam=50)
