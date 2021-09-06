n1=int(input('Primeira nota: '))
n2=int(input('Segunda nota: '))

print('a nédia é: {}'.format((n1+n2)/2))
if (n1+n2)/2>=6:
    print('Aluno aprovado')
else:
    print('Aluno reprovado')