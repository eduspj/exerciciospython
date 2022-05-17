def escreva(valor):
    tamanho = 4 + len(valor)
    print(f'~' * tamanho)
    print(f'{valor:^{tamanho}}')
    print(f'~' * (4 + len(valor)))


escreva('Eduardo dos Santos')
