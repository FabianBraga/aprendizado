m = []
for x in range(0, 3):
    linha = []
    for y in range(0, 3):
        iten= int(input(f'Digite um valor para [{x}, {y}]: '))
        linha.append(iten)
    m.append(linha[:])
pares = c3 = l2 = 0
print('-='*40)
for x in range(0, 3):
    for y in range(0, 3):
        print(f'[ {m[x][y]} ]', end='')
        if m[x][y] % 2 == 0:
            pares += m[x][y]
        if y == 2:
            c3 += m[x][y]
        if x == 1 and l2 == 0:
            l2 = m[x][y]
        if l2 < m[x][y] and x == 1:
            l2 = m[x][y]
    print('')
print('-='*40)

print(f'\nA soma de todos os valores paraes foi {pares}')
print(f'A soma de todos os valores da coluna 3 foi {c3}')
print(f'o maior valor na Linha 2 foi {l2}')
