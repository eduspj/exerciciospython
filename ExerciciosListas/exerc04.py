# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

vetor = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k']

for i, v in enumerate(vetor):
    if v not in 'aeiou':
        print(i, v)
