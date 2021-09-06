from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criaarquivo(arq)
else:
    print('Arquivo localizado e aberto...')

while True:
    opc = menu(['Cadastra uma pessoa','Listar pessoas','Sair do sistema'],40,4,0,5,0)
    if opc == 1:
        titulo('-','NOVO CADASTRO',40)
        nome = leia('nome: ','s',True,'Um nome deve ser informado')
        idade = leia('Idade: ','i',True,'Idade inválida')
        print(nome,idade)
        cadastrar(arq,nome,idade)
    elif opc == 2:
        lerarquivo(arq)
    elif opc == 3:
        print('escolhue 4')
    elif opc == 4:
        titulo('-','Sistema finalizado volte sempre!',40)
        break
