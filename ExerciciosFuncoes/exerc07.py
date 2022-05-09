"""
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores
para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou.
O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor
de prestação e assim continuar até que seja informado um valor igual a zero para a prestação.
este momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de
prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso,
cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
"""


def valorPagamento(valor, atraso):
    if atraso == 0:
        return valor
    else:
        multa = float(valor * 1.03 + (valor * (atraso * 0.001)))
        valor = multa
        return valor


qtd = 0
total = 0

continuar = False
while not continuar:
    prest = float(input('Digite a prestação: '))
    if prest == 0:
        continuar = True
    else:
        dias = float(input('Digite os dias em atraso: '))
        resultado = valorPagamento(prest, dias)
        print(resultado)
        print('=' * 40)
        qtd += 1
        total += resultado

print('#' * 40)
print('Relatório'.center(40))
print('#' * 40)
print(f'Foram pagos {qtd} prestações')
print(f'Total arecadado de R$ {total}')
print('#' * 40)
