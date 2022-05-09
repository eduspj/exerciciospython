"""
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
"""


def digitos(num):
    contador = 1
    aux = 0
    while num > 9.99:
        num = num / 10
        contador += 1
    print(contador)

digitos(98951)