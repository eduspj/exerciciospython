def leiaint():
    while True:
        aux = str(input('Digite um número inteiro: '))
        if not aux.isnumeric():
            print('ERRO! Digite um número inteiro válido.')
        else:
            return int(aux)


n = leiaint()
print(f'Digitou o número: {n}')
