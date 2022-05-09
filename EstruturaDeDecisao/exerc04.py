a = str(input('Digite uma letra: '))

if not a.isnumeric():
    if a not in 'AaEeIiOoUu':
        print('Consoante')
    else:
        print('vogal')
else:
    print('Não é letra')