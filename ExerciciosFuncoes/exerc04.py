"""
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
"""


def situacao(num):
    if num >= 0:
        return print('P')
    else:
        return print('N')


situacao(-58)