"""
desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve
receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20.
Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.
"""


def ret(l, a):
    if l > 20:
        l = 20
    if a > 20:
        a = 20
    print('-+-'*l)
    c =0
    while c < a:
        z = '|'
        print(f'{z}{z:>{(l*3 - 1)}}')
        c += 1
    print('-+-' * l)


l = int(input('Digite a largura: '))
a = int(input('Digite a altura: '))
ret(l, a)