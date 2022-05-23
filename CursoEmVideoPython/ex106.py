def ajuda(comando):
    help(comando)


while True:
    c = input('Função ou biblioteca: ').lower()
    if c == 'fim':
        break
    else:
        ajuda(c)
        