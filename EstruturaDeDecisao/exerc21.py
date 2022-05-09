# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
# quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor
# mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1

saque = int(input('Digite o valor do saque: '))

nota1 = 0
nota5 = 0
nota10 = 0
nota50 = 0
nota100 = 0
resto = saque

if resto >= 100:
    nota100 = int(resto/100)
    resto = resto % 100
if resto >= 50:
    nota50 = int(resto/50)
    resto = resto % 50
if resto >= 10:
    nota10 = int(resto / 10)
    resto = resto % 10
if resto >= 5:
    nota5 = int(resto / 5)
    resto = resto % 5
if resto >= 1:
    nota1 = resto

print(f'Saque de R$ {saque}')
print(f'{nota100} notas de 100')
print(f'{nota50} notas de 50')
print(f'{nota10} notas de 10')
print(f'{nota5} notas de 5')
print(f'{nota1} notas de 1')