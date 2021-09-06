def cadastro(texto,tipo='S',tamanho=99):
    if tipo.upper() == 'S':
        a = str(input(texto)[:tamanho])
    elif tipo.upper() == 'I':
        a = int(input(texto)[:tamanho])
    elif tipo.upper() == 'f':
        a = float(input(texto)[:tamanho])
    return a

def voto(ano = 0):
    """Função voto(ano) retorna uma strring com a resposta se a pessoa vota ou não
     no parametro é passado o ano de nascimento"""
    from datetime import datetime
    if ano ==0:
        ret = 'não foi passado um parametro'
    cal  = datetime.now().year-ano
    if cal <16:
        ret = f'com {cal} anos: NÂO VOTA.'
    elif 18<=cal<=65:
        ret = f'com {cal} anos: o voto é obrigatório.'
    else:
        ret = f'com {cal} anos: o voto é Opcional.'
    return ret

#programa principal
help(voto)
print(voto(cadastro('Em que ano você nasceu? ','i')))
