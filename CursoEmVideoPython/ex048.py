soma = 0
cont = 0
for i in range(1, 501):
    if i % 3 == 0 and i % 2 != 0:
        soma += i
        cont += 1

print(f'A soma de todos os {cont} valores é de {soma}')
