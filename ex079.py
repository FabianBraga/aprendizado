lista= []
while True:
    nm = int(input('digite um valor: '))
    if nm not in lista:
        lista.append(nm)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado! Não vou adicionar...')
    if input('Deseja continuar [S/N]: ') in 'Nn':
        break
lista.sort()
print(f'Esses foram os valores digitados {lista}')