lista = []
while True:
    if len(lista) == 0:
        aux = int(input('Digite um valor: '))
        lista.append(aux)
    else:
        aux = int(input('Digite um valor: '))
        for i in range(0, len(lista)):
            if aux == lista[i]:
                print('Já existe este numero!')
                break
            if (len(lista)-1) == i:
                lista.append(aux)
    continuar = input('Quer continuar: [S/N]: ').upper().strip()
    if continuar == 'N':
        break
print(lista)
print(sorted(lista))
