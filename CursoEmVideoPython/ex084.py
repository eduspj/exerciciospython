lista = []
matriz = []
pesado = []
leve = []
while True:
    lista.append(input('Nome: '))
    lista.append((float(input('Peso: '))))
    matriz.append(lista[:])
    if len(matriz) == 1:
        pesado.append(lista[:])
        leve.append((lista[:]))
    else:
        if pesado[0][1] == lista[1]:
            pesado.append(lista[:])
        elif pesado[0][1] < lista[1]:
            pesado.clear()
            pesado.append(lista[:])
        if leve[0][1] == lista[1]:
            leve.append(lista[:])
        elif leve[0][1] > lista[1]:
            leve.clear()
            leve.append(lista[:])
    lista.clear()
    continuar = input('Quer continuar [S/N]: ').upper()
    if continuar in 'Nn':
        break
print(f'Foram cadastradas {len(matriz)} pessoas')
print(f'Os mais pesados pesam {pesado[0][1]} e são: ', end='')
for i in pesado:
    print(f'[{i[0]}] ', end='')
print()
print(f'Os mais leves pesam {leve[0][1]} e são: ', end='')
for i in leve:
    print(f'[{i[0]}] ', end='')

