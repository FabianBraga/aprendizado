lista =[]
for x in range(1,6):
    lista.append(int(input(f'Informe o {x}º valor: ')))
print('='*50)
print(f'O maior valor foi: {max(lista)} ele está nas posiçãoes: ',end='')
for x ,y in enumerate(lista):
    if y == max(lista):
        print(f'{x}...',end='')
print(f'\nO menor valor foi: {min(lista)} ele está nas posições: ',end='')
for x ,y in enumerate(lista):
    if y == min(lista):
        print(f'{x}...',end='')
