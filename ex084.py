pessoas = []
galera = []
ct = menor = maior = 0
while True:
    pessoas.append(str(input('Informe o nome: ')))
    pessoas.append(float(input('Informe o Peso: ')))
    galera.append(pessoas[:])
    ct+=1
    if menor ==0:
        menor = pessoas[1]
        maior = pessoas[1]
    if pessoas[1] > maior:
        maior = pessoas[1]
    if pessoas[1] < menor:
        menor = pessoas[1]
    if input('Quer continuar [S/N]: ') in 'Nn':
        break
    pessoas.clear()
print(f'ao todo foram cadastradas {ct} pessoas')
print(f'O maior pesso foi de {maior:.2f}Kg. Peso de ',end='')
for p in galera:
    if p[1]== maior:
        print(f'[{p[0]}] ',end='')
print(f'\nO menor pesso foi de {menor:.2f}Kg. Peso de ',end='')
for p in galera:
    if p[1]== menor:
        print(f'[{p[0]}] ',end='')


