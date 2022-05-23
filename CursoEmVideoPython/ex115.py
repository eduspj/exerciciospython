def cabecalho(msg):
    print('-' * 40)
    print(f'{msg:^40}')
    print('-' * 40)


def listarpessoas():
    pass


def cadastrarpessoas(nome, idade):
    pass


def menu():
    cabecalho('MENU PRINCIPAL')
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova Pessoa')
    print('3 - Sair do sistema')
    print('-' * 40)


def numint():
    while True:
        op = str(input('Sua opção: '))
        if op.isnumeric():
            if op in '123':
                return op
            else:
                print('ERRO! Digite uma opção válida')
        else:
            print('EERO! por favor, digite um número inteiro válido.')


while True:
    menu()
    opc = numint()

    if opc == '3':
        break
    elif opc == '1':
        cabecalho('OPÇÃO 1')
    elif opc == '2':
        cabecalho('OPÇÃO 2')

