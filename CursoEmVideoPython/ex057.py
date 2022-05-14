sexo = input('informe seu sexo: [M/F]: ').upper().strip()

while sexo not in 'MF':
    print('Dados inválidos')
    sexo = input('informe seu sexo: [M/F]: ').upper().strip()
