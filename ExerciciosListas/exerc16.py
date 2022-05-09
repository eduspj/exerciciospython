"""
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana.
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja,
um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam
salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
"""

comissao = []
aux = 0
confirmar = False
faixa_i = 200
faixa_f = 299
qtd_func = 0

while not confirmar:
    aux = float(input('Digite as vendas: '))
    if aux == -1:
        confirmar = True
    else:
        comissao.append(200 + aux * 0.09)

for a in range(0, 9):
    for b in range(0, len(comissao)):
        if faixa_i < comissao[b] < faixa_f:
            qtd_func += 1
    if faixa_f > 999:
        print(f'Maior que $1000 = {qtd_func}')
    else:
        print(f'${faixa_i} - ${faixa_f} = {qtd_func}')
        qtd_func = 0
        faixa_i += 100
        faixa_f += 100

print(comissao)
