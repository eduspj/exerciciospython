from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'pessoas.txt'

if arquivo_existe(arq):
    print(f'Arquivo "{arq}" encontrado com sucesso')
else:
    print('Arquivo não encontrado')
    criar_arquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do sistema'])
    if resposta == 3:
        cabecalho('Saindo do Sistema... Até logo')
        break
    elif resposta == 1:
        cabecalho('Pessoas Cadastradas')
        ler_arquivo(arq)
    elif resposta == 2:
        cabecalho('Cadastrar nova pessoa')
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        cadastrar_pessoa(arq, nome, idade)
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)
