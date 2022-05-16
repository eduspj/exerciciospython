lista = []
par = []
impar = []

while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
    continuar = input('Quer continuar? [S/N]').upper().strip()
    if continuar in 'N':
        break
print(lista)
print(par)
print(impar)
