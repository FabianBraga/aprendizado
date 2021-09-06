from time import sleep
def titulo(msg,cor=0):
    c = ('\033[m',
         '\033[0;30;41m',   #1 -Vermelho
         '\033[0;30;42m',   #2 -verde
         '\033[0;30;43m',   #3 -amarelo
         '\033[0;30;44m',   #4 -azul
         '\033[0;30;45m',   #5 -roxo
         '\033[0;30;46m',)  #6 -branco

    print(c[cor],end='')
    print('~'*(len(msg)+4))
    print(f'  {msg}')
    print('~' * (len(msg)+4))
    print(c[0],end='')

def leia(texto, tipo='S', tamanho=99):
    """-> Retorna um contedudo recebido pelo teclado onde:
    texto = É o texto apresentado na tela para a inserção dos dados
    tipo = o tipo do valor de retorno pode ser 'i' , 's' ou 'f' onde:
        'i'= para valor inteiro por padrão é string
        's' = para string
        'f' = para float
    tamanho = A quantidade maxima de digitos permitido por padrão é 99"""

    if tipo.upper() == 'S':
        a = str(input(texto)[:tamanho])
    elif tipo.upper() == 'I':
        a = int(input(texto)[:tamanho])
    elif tipo.upper() == 'f':
        a = float(input(texto)[:tamanho])
    return a




#programa principal

while True:
    titulo('SISTEMA DE AJUDA PYHELP',2)
    text = leia('Função ou bibliotec > ')
    if text.upper() =='FIM':
        break
    titulo(f'acessando o manual do comando \'{text}\'',4)
    sleep(2)
    print(f'\033[47:30m')
    help(text)
