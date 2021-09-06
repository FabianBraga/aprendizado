nm = str(input('Insira a sua frase: ')).upper().strip()
print('existem {} letras "A" nessa frase'.format(nm.count('A')))
print('A primeira letra "A" apareceu na posição ',nm.find('A')+1)
print('A Ultima letra "A" apareceu na posição ',nm.rfind('A')+1)