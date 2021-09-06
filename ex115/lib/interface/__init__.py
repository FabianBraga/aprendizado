#Função de cores
def cor(fre=0,fun=0):
    """
    -> Função que define cores de saída para impressão
    :param fre: define a cor da frente, valores possíveis de 0 a 7 o valor defalt é 0
    :param fun: efine a cor do fundo, valores possíveis de 0 a 7 o valor defalt é 0
    0 - para a letre o valor é Branco e para o fundo sem cor
    1 - preto
    2 - vermelho
    3 - verde
    4 - amarelo
    5 - azul
    6 - roxo
    7 - ciano
    8 - cinza
    """
    if 0>fre>8:
        fre = 0
    if 0>fun>8:
        fun = 0
    fe = ('',30,31,32,33,34,35,36,37)
    fu = ('',40,41,42,43,44,45,46,47)
    if fun ==0:
        ret = f'\033[;{fe[fre]}m'
    else:
        ret = f'\033[;{fe[fre]};{fu[fun]}m'
#    print(f'{ret}',end='')
    return ret


#Função de entrada de dados
def leia(texto='Entre com os dados: ', tipo='S',obg=False,msgvalid ='Este campo é de preenchimento obrigatório, informe um valor válido!' ):
    """
    -> Retorna um contedudo recebido pelo teclado onde:
    texto = É o texto apresentado na tela para a inserção dos dados
    tipo = o tipo do valor de retorno pode ser 'i' , 's' ou 'f' onde:
        'i'= para valor inteiro por padrão é string
        's' = para string
        'f' = para float
    obg = Define se o campo é obrigatório ou não, por padrão o campo não é obrigatório
    msgvalid = 'Menssagem de retorno em caso de erro de digitação se não informado assume o texto padrão

    obs: caso não tenha ativado a validação e informar tipo I ou F inválidos o retorno vai ser 0
         caso informe um tipo não listado a função assume o valor como S
    """
    if tipo.upper() not in 'SIF':
        tipo = 'S'
    else:
        tipo = tipo.upper()
    if obg:
        while True:
            if tipo in 'F':
                a = str(input(texto)).replace(',','.').strip()
            else:
                a = str(input(texto))
            if tipo in 'FI':
                for x in a:
                    if not x.isnumeric() and x!='.':
                        a=''
                        break
            if a !='':
                if tipo =='I':
                    a = int(a)
                elif tipo == 'F':
                    a = float(a)
            if str(a) == '':
                print(cor(fre=2),msgvalid,cor())
            else:
                break
    else:
        if tipo == 'S':
            a = str(input(texto))
        elif tipo in 'IF':
            a = str(input(texto)).replace(',', '.').strip()
            for x in a:
                if not x.isnumeric() and x != '.':
                    a = ''
                    break
            if a !='':
                if tipo =='I':
                    a = int(a)
                elif tipo == 'F':
                    a = float(a)
            else:
                a = 0
    return a

def centra(msg,tm=50):
    ret = f'{" "*(round((tm-len(msg))/2))}{msg}'
    return ret

#Função de títulos
def titulo(linha='-', msg='', tam=50,corl=0,corf=0):
    """
    -> função que imprime um titulo na tela que pode ser colorido
    :param c: define o caracter a ser utilizado como linha de ceparação
    :param msg: Mensagem a ser exibida
    :param tam: largura do titulo
    :param corl: cor da letra
    :param corf: cor do fundo
    as cores varia conforme a tabela abaixo:
    0 - para a letre o valor é Branco e para o fundo sem cor
    1 - preto
    2 - vermelho
    3 - verde
    4 - amarelo
    5 - azul
    6 - roxo
    7 - ciano
    8 - cinza

    """
    print(cor(corl,corf),end='')
    print(linha * (tam))
    if msg !='':
        print(centra(msg,tam*len(linha)))
        print(linha * (tam))
    print(cor(),end='')

def menu(lista,linha=20,cornumLetra= 0,cornumFundo=0,cortexletra = 0,cortexfundo=0):
    """
    ->Apresenta um menu na tela
    :param lista: uma lista passada pelo parâmetro
    :return:
    """
    titulo('-','MENU PRINCIPAL',linha)
    c= 1
    for x in lista:
        print(f'{cor(cornumLetra,cornumFundo)}{c}  -{cor()}  {cor(cortexletra,cortexfundo)}{x}{cor()}')
#        print(f'{c}  -  {x} )
        c += 1
    titulo('-',tam=linha)
    while True:
        opc=leia('Sua opção: ','i',True)
        if 1<= opc <= c:
            break
        else:
            print('Opção inválida')
    return opc

