lista= []
par = []
impar = []
while True:
    nm = int(input('digite um valor: '))
    lista.append(nm)
    if input('Deseja continuar [S/N]: ') in 'Nn':
        break
for x in lista:
    if x%2 == 0:
        par.append(x)
    else:
        impar.append(x)
print('-=-'*40)
print(f'Esses foram os valores digitados {lista}')
print(f'Esses foram os valores Pares digitados {par}')
print(f'Esses foram os valores impares {impar}')