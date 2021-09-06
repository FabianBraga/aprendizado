nm = str(input('Informe seu nome: ')).strip()
print('Muito prazer em te conhecer\nSeu primeiro nome é ',nm[:nm.find(' ')])
print('Seu último nome é ', nm[nm.rfind(' '):])