m = []
for x in range(0, 3):
    linha = []
    for y in range(0, 3):
        iten= int(input(f'Digite um valor para [{x}, {y}]: '))
        linha.append(iten)
    m.append(linha[:])
for x in range(0,3):
    for y in range(0,3):
        print(f'[ {m[x][y]:^5} ]',end='')
    print('')
