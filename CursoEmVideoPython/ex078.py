lista = []
maior = 0
menor = 0
for i in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
    if len(lista) == 1:
        maior = menor = lista[0]
    if lista[i] > maior:
        maior = lista[i]
    if lista[i] < menor:
        menor = lista[i]
print(lista)
print(f'O maior valor digitado foi {maior} e aparece nas posições: ', end=" ")
for i, j in enumerate(lista):
    if j == maior:
        print(i, end=' ')
print()
print(f'O menor valor digitado foi {menor} e aparece nas posições: ', end=" ")
for i, j in enumerate(lista):
    if j == menor:
        print(i, end=' ')
