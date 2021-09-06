lista = list()
while True:
    aluno = str(input("Nome: "))
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))
    media = (nota1+nota2)/2
    lista.append([aluno,[nota1,nota2],media])
    if input('Quer continuar [S/N]: ') in 'Nn':
        break
print('-='*30)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('-'*26)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
while True:
    print('-'*35)
    opc = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('-*'*35)
        print('Finalizado')
        break
    if opc <= len(lista) -1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
print('Volte sempre')