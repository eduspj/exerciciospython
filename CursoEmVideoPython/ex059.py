def somar(x, y):
    return print(f'{x} + {y} é {x + y}')


def multiplicar(x, y):
    return print(f'{x} * {y} é {x * y}')


def maior(x, y):
    if x > y:
        return print(f'{x} é maior de {y}')
    else:
        return print(f'{y} é maior de {x}')


valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))

continuar = True
while continuar:
    print(f'[ 1 ] somar\n'
          f'[ 2 ] multiplicar\n'
          f'[ 3 ] maior\n'
          f'[ 4 ] novos números\n'
          f'[ 5 ] sair do programa')
    opc = int(input('>>>> Qual é sua opção: '))
    if opc == 1:
        somar(valor1, valor2)
    elif opc == 2:
        multiplicar(valor1, valor2)
    elif opc == 3:
        maior(valor1, valor2)
    elif opc == 4:
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    elif opc == 5:
        continuar = False
