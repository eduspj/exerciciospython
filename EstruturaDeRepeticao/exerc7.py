# Faça um programa que leia 5 números e informe o maior número.

aux = 0
soma = 0
media = 0

for a in range(1, 6):
    num = int(input(f'Digite o {a} número: '))
    soma += num
    if num > aux:
        aux = num


print(f'Maior número é {aux}')
print(f'Soma dos números é {soma}')
print(f'Média dos números é {soma / 5}')



