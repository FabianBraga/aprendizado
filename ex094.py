cadastro=[]
pessoa = {}
idades = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Informe o sexo [M/F]: ').upper()[0])
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('Sexo inválido tente novamente!!')

    pessoa['ano'] = int(input('Idade: '))
    idades += int(pessoa['ano'])
    cadastro.append(pessoa.copy())
    if input('Quer continuar [S/N]: ') in 'Nn':
        break
média = idades /len(cadastro)
print('-='*30)
print(f'O grupo tem {len(cadastro)} pessoas cadastradas.')
print(f'A média de ano do grupo é de {média:5.2f} anos.')
print(f'As mulheres cadastradas foram: ',end='')
for x in cadastro:
    if x['sexo'] in 'F':
        print(f'{x["nome"]} ',end='')
print('\nLista das pessoas que estão acima da média')
for x in cadastro:
    if x['ano'] >= média:
        print('      ')
        for c, d in x.items():
            print(f'{c} = {d}; ',end='')
