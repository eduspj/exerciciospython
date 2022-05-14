num = 24
cont = 0
for i in range(1, num + 1):
    if num % i == 0:
        cont += 1
        print(i, end=' ')
if cont == 2:
    print(f'É numero primo')
else:
    print('Não é primo')