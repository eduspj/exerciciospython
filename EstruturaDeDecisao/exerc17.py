# Faça um Programa que peça um número correspondente a um determinado ano e em seguida
# informe se este ano é ou não bissexto
# Para saber quando será ano bissexto deve-se seguir o seguinte princípio: todos os anos múltiplos de 4 que também não são
# múltiplos de 100, com exceção dos múltiplos de 400, deverão ser anos bissextos. Por exemplo, 2004 e 2008 são múltiplos
# de 4 e, por este motivo, considerados anos bissextos. No entanto, 1900 e 1700 não foram anos bissextos,
# pois eram múltiplos de 100.

ano = int(input('Digite um ano (yyyy): '))


if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'O ano de {ano} é bissexto. ')
        else:
            print(f'O ano de {ano} NÃO é bissexto. ')
    else:
        print(f'O ano de {ano} é bissexto.')
else:
    print(f'O ano de {ano} NÃO é bissexto. ')

