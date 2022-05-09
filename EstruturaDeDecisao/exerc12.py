# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
# Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto
# menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as
# informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

valor_hora = float(input('Digite o valor da hora R$ '))
horas_trabalhadas = int(input('Digite as horas trabalhadas no mês: '))
desconto_ir = 0
salario_bruto = valor_hora * horas_trabalhadas
sindicato = salario_bruto * 3 / 100
fgts = salario_bruto * 11 / 100
inss = salario_bruto * 10 / 100
salario_liquido = 0

if 900 <= salario_bruto < 1500:
    desconto_ir = 5
elif 1500 <= salario_bruto < 2500:
    desconto_ir = 10
elif salario_bruto >= 2500:
    desconto_ir = 20

valor_ir = salario_bruto * desconto_ir / 100
total_descontos = valor_ir + inss
salario_liquido = salario_bruto - total_descontos


print()
print(f'\t\tSalário bruto: ({valor_hora} * {horas_trabalhadas})          : R$')
print(f'{salario_bruto}')
print(f'    (-) IR ({desconto_ir}%)                             : R$')
print(f'{valor_ir}')
print(f'    (-) INSS ( 10%)                         : R$')
print(f'{inss}')
print(f'    FGTS (11%)                              : R$')
print(f'{fgts}')
print(f'        TOTAL DE DESCONTOS                  : R$')
print(f'{total_descontos}')
print(f'        Salário Liquido                    : R$')
print(f'{salario_liquido}')


