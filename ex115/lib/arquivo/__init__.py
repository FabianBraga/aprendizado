from ex115.lib.interface import *
def arquivoexiste(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criaarquivo(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print('Ocorreu um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerarquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        titulo('-','PESSOAS CADASTRADAS',40)
        for x in a:
            dado = x.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq,nome='desconhecido',idade=0):
    try:
        a = open(arq,'at')

    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
            print('passei na gravação')
        except:
            print('Houve um erro na gravação do arquivo')
        else:
            print(f'Novo registro de {nome} adicionado.')