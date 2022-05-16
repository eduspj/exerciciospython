lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    while True:
        continuar = input('Quer continuar? [S/N]: ').upper().strip()
        if continuar in 'SsNn':
            break
    if continuar == 'N':
        break
print(lista)
reverso = sorted(lista, reverse=True)
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)}')
print(f'{reverso}')
print(f'{lista}')
