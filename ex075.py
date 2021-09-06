from random import randint
temp= ''
ct9 = ct_par =0
for x in range(0,4):
    vl = int(input('Digite um valor: '))
    temp += str(vl)

c  = tuple(temp)
print(f'você digitou os valores: {temp}')
for x in c:
    if int(x)==9:
        ct9 += 1
    if int(x)%2 == 0:
       ct_par += 1
print(f'O valor 9 apareceu {ct9} vezes')
if temp.count('3') == 0 :
    print('o numero 3 não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 apareceu na {temp.index("3")+1}ª posição')
print(f'Os valores pares digitados foram: ',end='')
for x in temp:
    if int(x)%2 == 0:
        print(f'{x} ',end='')