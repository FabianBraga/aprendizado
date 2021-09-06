print('-'*50)
print(f'{"LOJA SUPER BARATÃO":^50}')
print('-'*50)
tot = totmil = menor = cont = 0
barato = ' '
while True:
    produto = input('Informe o nome do produto: ')
    preco = float(input('Informe o valor do produto: '))
    resp = ' '
    tot += preco
    cont += 1
    if preco >1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    while resp not in 'SN':
        resp = input('Quer continuar [S/N]: ').strip().upper()[0]
    if resp == 'N':
        break
print('-'*50)
print(f'{"FIM DO PROGRANA":^50}')
print(f'O total da compra foi de: {tot:.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1000,00')
print(f'O produto mais barato foi {barato}, que custou {menor:.2f}')
