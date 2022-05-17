from random import randint


def sorteia(lista):
    for i in range(0, 5):
        lista.append(randint(1, 10))


def somapar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(soma)


numeros = []
sorteia(numeros)
print(numeros)
somapar(numeros)
