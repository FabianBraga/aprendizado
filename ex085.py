lista = [[],[]]
valor = 0
for x in range(1,8):
    valor = (int(input(f'Informe o {x}º valor: ')))
    if (valor % 2) == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores impares digitados foram: {lista[1]}')
