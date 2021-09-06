exp = input('Entre com a expressão matemática: ')
vl = 0
ct_abre = 0
for x in exp:
    if x =='(':
        vl += 1
    elif x ==')':
        vl -= 1
    if x == ')' and vl< 0:
        print('Sua expressão está errada')
        break
if vl == 0:
    print('sua expressão está correta')