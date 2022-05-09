"""
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
"""


def imprima(n):
    for a in range(1, n + 1):
        print()
        for b in range(1, a + 1):
            print(a, end=" ")


imprima(5)
