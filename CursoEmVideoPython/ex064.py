n = int(input('Digite um númeero[999 para parar]: '))
soma = 0
cont = 0
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um númeero[999 para parar]: '))
print(f'Você digitou {cont} números e a soma é {soma}')
