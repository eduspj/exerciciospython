# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input('Digite o preço do 1º produto R$ '))
produto2 = float(input('Digite o preço do 2º produto R$ '))
produto3 = float(input('Digite o preço do 3º produto R$ '))

if produto1 < produto2:
    if produto1 < produto3:
        print(f'O produto 1 é mais barato R$ {produto1}')
    else:
        print(f'O produto 3 é mais barato R$ {produto3}')
else:
    if produto2 < produto3:
        print(f'O produto 2 é mais barato R$ {produto2}')
    else:
        print(f'O produto 3 é mais barato R$ {produto3}')