from datetime import datetime
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
cadastro['nasc'] = int(input('Ano de nascimento: '))
cadastro['ctps'] = int(input('Ctps: '))
cadastro['ano'] = datetime.now().year-cadastro['nasc']
if cadastro['ctps'] != 0:
    cadastro['ano'] = int(input('Informe o ano de contratação: '))
    cadastro['salario'] = int(input('Informe o sálario: '))
    cadastro['aposenta'] =(cadastro['ano']+cadastro['ano']+35)-datetime.now().year
print('-='*50)
for x, y in cadastro.items():
    print(f'   ---{x} tem o valor {y}')
