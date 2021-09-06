#Função de cores
def cor(fre=0,fun=0):
    """
    -> Função que define cores de saída para impressão
    :param fre: define a cor da frente, valores possíveis de 0 a 7 o valor defalt é 0
    :param fun: efine a cor do fundo, valores possíveis de 0 a 7 o valor defalt é 0
    0 - sem cor
    1 - vermelho
    2 - verde
    3 - amarelo
    4 - azul
    5 - roxo
    6 - branco
    """
    if 0>fre>7:
        fre = 0
    if 0>fun>7:
        fun = 0
    fe = ('',30,31,32,33,34,35,36,37)
    fu = ('',40,41,42,43,44,45,46,47)
    if fun ==0:
        ret = f'\033[;{fe[fre]}m'
    else:
        ret = f'\033[;{fe[fun]};{fu[fun]}m'

    return ret

#Função de entrada de dados
def leia(texto, tipo='S', tamanho=99,e=False):
    """
    -> Retorna um contedudo recebido pelo teclado onde:
    texto = É o texto apresentado na tela para a inserção dos dados
    tipo = o tipo do valor de retorno pode ser 'i' , 's' ou 'f' onde:
        'i'= para valor inteiro por padrão é string
        's' = para string
        'f' = para float
    tamanho = A quantidade maxima de digitos permitido por padrão é 99
    e = Define se o campo é obrigatório ou não, por padrão o campo não é obrigatório
    """
    if not e:
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
    else:
        while True:
            if tamanho == 99:
                a = str(input(texto))
            else:
                a = str(input(texto))[tamanho]
            if a.isnumeric():
                if tipo =='i':
                    a = int(a)
                elif tipo == 'f':
                    a = float(a)
            if str(a) == '':
                print('Este campo é de preenchimento obrigatório, informe um valor válido!')

    return a
#Função de títulos
def titulo(msg):
    print('-'*(len(msg)+4))
    print(f'  {msg}')
    print('-' * (len(msg)+4))


#teste de funções

print(cor(5),'teste de cores')