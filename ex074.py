from random import sample
temp= tuple(sample(range(10), 5))
print(f'Os numeros sorteados foram: ',end='')
for x in temp:
    print(f'{x} ',end='')
print(f'\nO menor valor sorteado foi: {max(temp)}')
print(f'O maior valor sorteado foi: {min(temp)}')

#for x in range(0,5):
#    temp += str(randint(1,10))

#c  = tuple(temp)
#nm_menor = nm_maior = 0

#print(f'Os numeros sorteados foram: ',end='')
#for x in range(0,5):
#    if x == 0:
#        nm_maior = temp[x]
#        nm_menor = temp[x]
#    else:
#        if nm_menor > temp[x]:
#            nm_menor = temp[x]
#        if nm_maior < temp[x]:
#            nm_maior = temp[x]
#    print(f' {int(temp[x])}', end='')

#print(f'\nO menor valor sorteado foi: {nm_menor}')
#print(f'O maior valor sorteado foi: {nm_maior}')
