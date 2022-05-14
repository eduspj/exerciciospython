contador = 0
media = 0
maior = 0
menor = 0
soma = 0
continuar = True

while continuar:
    numero = int(input('Digite um número: '))
    contador += 1
    soma += numero
    if contador == 1:
        maior = menor = numero
    elif numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    opc = str(input('Quer continuar? [S/N]: ')).upper().strip()
    while opc not in 'SsNn':
        opc = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if opc == 'N':
        continuar = False
media = soma / contador
print(f'Você digitou {contador} números com média de {media}')
print(f'O menor valor foi {menor} e o maior {maior}')
