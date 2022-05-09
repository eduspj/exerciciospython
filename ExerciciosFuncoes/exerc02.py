"""
Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
"""


def valor(n):
    for a in range(0, n + 1):
        print()
        for b in range(0, a):
            print(b+1, end=" ")


valor(7)
