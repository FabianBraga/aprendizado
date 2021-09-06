def notas(*n,sit = False):
    """->Função que avalia uma relação de notas e extrai a melhor e a pior nota dos alunos
    onde n é uma relação de notas passadas para a função
    onde sit é um valor opcional se sit = True mostra a situação"""
    if n != ():
        ret = dict()
        ret ['total'] = len(n)
        ret['maior'] = max(n)
        ret['menor'] = min(n)
        ret['média'] = sum(n)/len(n)
        if sit:
            if ret['média'] < 5:
                ret['Situação']= 'RUIM'
            elif 5 <= ret['média'] <7:
                ret['Situação'] = 'RAZOÁVEL'
            else:
                ret['Situação'] = 'BOA'
    else:
        ret = ''

    return ret


#programa principal
print(notas(4,5,6,7,8))
help(notas)
