from random import randint

while True:
    valor = int(input('Digite um valor: '))
    par_ou_impar = input('Par ou impar? [P/I]: ').upper()
    computador = randint(0, 11)
    soma = valor + computador
    if par_ou_impar == 'P':
        if (valor + computador) % 2 == 0:
            print(f'Você jogou {valor} e o computador jogou {computador} = {soma}, deu PAR você ganhou!')
        else:
            print(f'Você jogou {valor} e o computador jogou {computador} = {soma}, deu IMPAR você perdeu!')
            break
    elif par_ou_impar == 'I':
        if (valor + computador) % 2 != 0:
            print(f'Você jogou {valor} e o computador jogou {computador} = {soma}, deu IMPAR você ganhou!')
        else:
            print(f'Você jogou {valor} e o computador jogou {computador} = {soma}, deu PAR você perdeu!')
            break
