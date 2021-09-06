from random import randint
print('=-'*25)
print('Vamos jogar par ou impar?'.upper())
print('=-'*25)
ct = 0
vc  = 0
while True:
    vl = int(input('Digite um valor: '))
    op = str(input('Escolha [P/I]: ')).strip().upper()
    pc = randint(1,10)
    if op == 'P' :
        if (pc+vl) % 2 == 0:
            vc = 1
        else:
            vc = 0
    elif op == 'I':
        if (pc+vl) % 2 != 0:
            vc = 1
        else:
            vc = 0
    else:
        print('Opção inválida')
        vc = 21
    print('-'*50)
    if vc == 0:
        print('Você \033[31m PREDEU! \033[m')
        print(f'Você jogou {vl} o computador {pc}. Total {vl+pc} deu {"Par" if (vl+pc)% 2== 0 else "Impar":} ')
        print(f'Você venceu {ct} partidas')
        break
    elif vc == 1:
        print(f'Você jogou {vl} o computador {pc}. Total {vl+pc} deu {"Par" if (vl+pc)% 2== 0 else "Impar":} ')
        print(f'''Você \033[34mVenceu!!!\033[m 
        Vamos jogar outra partida... ''')

        ct += 1
    print('-'*50)
