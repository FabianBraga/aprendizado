fr = str(input('Entre coma a frase: ')).upper().replace(' ','')
op = ''
for x in range(len(fr),0,-1):
    op += fr[x-1]
if fr == op:
    print('Temos um palidromo')
else:
    print('Essa frase não é um palidromo')