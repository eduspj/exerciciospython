print(20 * '-=')
print('         Sequência de FIBONACCI')
print(20 * '-=')
termos = int(input('Quantos termos vc quer mostrar: '))
termo0 = 0
termo1 = 1
soma = 0
cont = 2
print(f'{0}->{1}', end='->')
while cont < termos:
    soma = termo0 + termo1
    print(f'{soma}', end='->')
    termo0 = termo1
    termo1 = soma
    cont += 1
print('FIM')
