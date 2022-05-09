"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)
    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer
    input <- Nova tarefa
"""


def menu():
    print('-' * 30)
    print(f'1 - Adicionar tarefa')
    print(f'2 - Listar tarefas')
    print(f'3 - Desfazer tarefa')
    print(f'4 - Refazer tarefa')
    print(f'5 - Sair')
    print('-' * 30)


def opc(opcao):
    if opcao == 1:
        pass
    elif opcao == 5:
        return False


def nova_tarefa():
    tarefas.append(input('Adicione uma tarefa: '))


def listar_tarefas():
    for i in tarefas:
        print(i)


def desfazer_tarefa():
    if len(tarefas) > 0:
        lixeira.append(tarefas[len(tarefas)-1])
        tarefas.pop()


def refazer_tarefa():
    if len(lixeira) != 0:
        tarefas.append(lixeira[len(lixeira)-1])
        lixeira.pop()


if __name__ == '__main__':
    tarefas = []
    lixeira = []
    continuar = True
    opcao = 0

    while continuar:
        menu()
        opcao = int(input('Digite a opção: '))
        print('*' * 30)
        if opcao == 1:
            nova_tarefa()
        elif opcao == 2:
            listar_tarefas()
        elif opcao == 3:
            desfazer_tarefa()
        elif opcao == 4:
            refazer_tarefa()
        elif opcao == 5:
            continuar = False



