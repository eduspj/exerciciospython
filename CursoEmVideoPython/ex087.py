matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
cont = 1
soma = coluna3 = maiorlinha2 = 0

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite o {cont}º valor: '))
        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j]
        if j == 2:
            coluna3 += matriz[i][j]
        if i == 1 and matriz[i][j] > maiorlinha2:
            maiorlinha2 = matriz[i][j]
        cont += 1
print('-=' * 30)
for i in matriz:
    for j in range(0, 3):
        print(f'[ {i[j]} ]', end='')
        if j == 2:
            print()
print('-=' * 30)
print(f'A soma dos números pares é de {soma}')
print(f'A soma dos números da 3ª coluna é de {coluna3}')
print(f'O maior número da linha 2 é {maiorlinha2}')
