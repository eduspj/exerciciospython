"""
Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter
 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e
uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para
efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
"""


def converter(h, m):
    sigla = ''
    if h == 0 or h == 12:
        if h == 0:
            sigla = 'A'
            h = 12
        else:
            sigla = 'P'
    else:
        if h > 12:
            h -= 12
            sigla = 'P'
        else:
            sigla = 'A'
    impressao(h, m, sigla)


def impressao(h, m, sigla):
    print(f'{h}:{m} {sigla}M')


continuar = False
while continuar == False:
    print('='*30)
    horas = int(input('Digite as horas: '))
    minutos = int(input('Digite os minutos: '))
    converter(horas, minutos)
    print('=' * 30)
    opcao = input('Quer continuar? (S/N)')
    if opcao in 'Nn':
        continuar = True
