from func import cor
def leiaint(texto):
    """-> Retorna um contedudo recebido pelo teclado onde:
    texto = É o texto apresentado na tela para a inserção dos dados"""
    while True:
        try:
            a = str(input(texto))
            if a.isnumeric():
                a = int(a)
                break
            else:
                print('\033[:31mErro! Digite um numero inteiro válido\033[m')
                continue
        except (ValueError,TypeError):
            print(cor(1,0),'Erro! por favor , digite um numero inteiro válido',cor())
        except (KeyboardInterrupt):
            print(cor(1,0),'Usuario preferiu não digitar essa valor ',cor())
            return 0
        else:
            return a


#programa de teste

num = leiaint('Digite um valor: ')
print(f'O valor digitado foi {num}')