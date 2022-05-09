"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""


def somente_numeros(valor):
    num = []
    for i in valor:
        if i.isnumeric():
            if len(num) != 12:
                num.append(i)
    return num


def gerar_digito(v_cnpj):
    digito1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    digito2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = 0
    dig1 = '0'
    dig2 = '0'
    for i, j in enumerate(v_cnpj):
        soma += int(v_cnpj[i]) * int(digito1[i])
    if (11 - (soma % 11)) < 10:
        dig1 = str(11 - (soma % 11))
    v_cnpj.append(dig1)
    soma = 0
    for x, y in enumerate(v_cnpj):
        soma += int(v_cnpj[x]) * int(digito2[x])
    if (11 - (soma % 11)) < 10:
        dig2 = str(11 - (soma % 11))

    return print(f'Digitos são {dig1, dig2}')


cnpj = '40.688.134/0001-61'
cnpj_so_num = []
cnpj_novo = ''
soma = 0

if __name__ == '__main__':
    cnpj_so_num = somente_numeros(cnpj)
    gerar_digito(cnpj_so_num)
