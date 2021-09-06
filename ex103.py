def ficha(jog='<desconhecido>',gol=0):
    resposta = f'O jogador {jog} fez {gol} gol(s) no campeonato'
    return resposta

def leia(texto, tipo='S', tamanho=99):
    """
    -> Retorna um contedudo recebido pelo teclado onde:
    texto = É o texto apresentado na tela para a inserção dos dados
    tipo = o tipo do valor de retorno pode ser 'i' , 's' ou 'f' onde:
        'i'= para valor inteiro por padrão é string
        's' = para string
        'f' = para float
    tamanho = A quantidade maxima de digitos permitido por padrão é 99"""
    if tipo.upper() == 'S':
        if tamanho == 99:
            a = str(input(texto))
        else:
            a = str(input(texto)[tamanho])
    elif tipo.upper() == 'I':
         a = str(input(texto)).strip()
         if a.isnumeric():
             a = int(a)
         else:
             a = 0
    elif tipo.upper() == 'f':
        a = float(input(texto)[:tamanho])
    return a


#Programa principal
jogador = leia('Nome do jogador: ')
gols = leia('Número de gols: ','i')
if jogador.strip() =='':
    print(ficha(gol=gols))
else:
    print(ficha(jogador,gols))
