# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele
# que é divisível somente por ele mesmo e por 1.

num = int(input('Digite um número: '))
contador = 0

for a in range(num, 0, -1):
    if num % a == 0:
        contador += 1
        print(f'Divisivel por {a}')

if contador > 2:
    print('Não é número primo')
else:
    print('É número primo')