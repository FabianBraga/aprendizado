alunos = {}
alunos['nome'] = str(input('Nome: '))
alunos['media'] = float(input(f'Média de {alunos["nome"]}: '))

print(f'Nome é igual a {alunos["nome"]}')
print(f'Média é igual a {alunos["media"]}')
if alunos['media'] >= 7:
    alunos['situação'] = 'Aprovado'
else:
    alunos['situação'] = 'Reprovado'

print(f'Situação é igual a {alunos["situação"]}')