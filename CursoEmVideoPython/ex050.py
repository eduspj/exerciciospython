soma = 0
aux = 0
for i in range(1, 7):
    aux = int(input(f'Digite o {i}º número: '))
    if i % 2 == 0:
        soma += aux

print(soma)
