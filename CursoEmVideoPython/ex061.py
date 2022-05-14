primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 0
termos = 10
mostrados = 0

while termos != 0:
    mostrados += termos
    while cont < termos:
        print(f'{primeiro_termo}', end='->')
        primeiro_termo += razao
        cont += 1
    print('PAUSA')
    termos = int(input('Quantos termos quer mostrar a mais? '))
    cont = 0
print(f'Progressão finalizada com {mostrados} termos mostrados')
