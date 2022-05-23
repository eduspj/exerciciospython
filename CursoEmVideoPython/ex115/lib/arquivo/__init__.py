def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        if not arquivo_existe(nome):
            a = open(nome, 'wt+')
            a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo "{nome}" criado com sucesso')


def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler arquivo')
    else:
        a.seek(0, 0)  # Coloca o cursor no início do arquivo
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<32}{dado[1]:>5} anos')

    finally:
        a.close()


def cadastrar_pessoa(arq, nome, idade):
    try:
        a = open(arq, 'at')
    except:
        print('ERRO ao ler arquivo')
    else:
        a.writelines(f'{nome};{idade}\n')
        print(f'Novo registro de {nome} adicionado ')
    finally:
        a.close()
