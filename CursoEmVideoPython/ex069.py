mais18 = 0
homens = 0
mulheres_menos_20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F]: ').upper().strip()
    while sexo not in 'MmFf':
        sexo = input('Sexo: [M/F]: ').upper().strip()
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
    print('-=' * 20)
    continuar = input('Quer continuar? [S/N]: ').upper().strip()
    while continuar not in 'SsNn':
        continuar = input('Quer continuar? [S/N]: ').upper().strip()
    print('-=' * 20)
    if continuar == 'N':
        break

print(f'Mais de 18 {mais18}')
print(f'Homens cadastrados {homens}')
print(f'Mulheres com menos de 20 {mulheres_menos_20}')