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
lista.sort(reverse=True)
print('-=-'*30)
print(f'Você digitou {len(lista) } elementos.')
print(f'Esses foram os valores digitados {lista}')
if 5 in lista:
    print('O valor 5 faz parte da cadastro!')
else:
    print('O valor 5 não foi encontrado nessa cadastro!')
