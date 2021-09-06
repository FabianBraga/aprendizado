def leiaint(texto):
    """-> Retorna um contedudo recebido pelo teclado onde:
    texto = É o texto apresentado na tela para a inserção dos dados"""
    while True:
        a = str(input(texto))
        if a.isnumeric():
            a = int(a)
            break
        else:
            print('\033[:31mErro! Digite um numero inteiro válido\033[m')
        print('erro')
    return a

#Programa principal


var = leiaint('Entre com um numero: ')