# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para
# desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = float(input('Qual o salário do colaborador? '))
percentual = 0
valor = 0
novo_salario = 0

if salario < 280:
    percentual = 20
elif 280 <= salario < 700:
    percentual = 15
elif 700 <= salario < 1500:
    percentual = 10
elif salario >= 1500:
    percentual = 5

valor = salario * percentual / 100
novo_salario = salario + valor

print(f'Salário do colaborador R$ {salario}')
print(f'Percentual de aumento de {percentual}%')
print(f'Colaborador vai de ter um aumento de R$ {valor}')
print(f'Novo salário do colaborador R$ {novo_salario}')

