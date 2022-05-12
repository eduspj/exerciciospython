valor_casa = 80000
salario = 1400 * 30 / 100
anos = 15 * 12
financ = valor_casa / anos
prestacao_minima = financ < salario

if prestacao_minima:
    print(f'Financiamento aprovado {anos} x {salario}')
else:
    print(f'Financiamento recusado')
print(prestacao_minima)
