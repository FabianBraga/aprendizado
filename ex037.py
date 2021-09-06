nm = str(input('Informe o numero inteira para a conversão: ')).strip()
op=4
while op <0 or op > 3:
    op= int(input('infore:\n1 para Binária\n2 para Octal\n3 para Hexadecinal\n\033[;33mEntre com a sua opção:\033[m '))
    if op <0 or op > 3:
        print('Opção inválida telte novamente...')
if op == 1:
    div = int(nm)
    res=''
    cap=''
    while div+1>= 2:
        cap = cap+ str(div % 2)
        div = div // 2
    x = 1
    while x <= len(cap):
        res = res + cap[(len(cap)-x)]
        x= x+1
    print('o resultado em binário é : ',res)
elif op == 2:
    div = int(nm)
    res=''
    cap=''
    while div+7>= 8:
        cap = cap+ str(div % 8)
        div = div // 8
    print(cap)
    x = 1
    while x <= len(cap):
        res = res + cap[(len(cap)-x)]
        x= x+1
    print('o resultado em octal é : ',res)
else:
    div = int(nm)
    res=''
    cap=''
    while div+15>= 16:
        if div % 16<10:
            cap = cap+ str(div % 16)
        else:
            if div % 16==10:
                cap = cap +'A'
            elif div % 16 == 11:
                cap = cap + 'B'
            elif div % 16==12:
                cap = cap + 'C'
            elif div % 16==13:
                cap = cap + 'D'
            elif div % 16==14:
                cap = cap + 'E'
            else:
                cap = cap + 'F'
        div = div // 16
    x = 1
    while x <= len(cap):
        res = res + cap[(len(cap)-x)]
        x= x+1
    print('o resultado em Hexadecimal é : ',res)


