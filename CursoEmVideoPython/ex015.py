km = float(input('Digite os kms rodados: '))
dias = int(input('Digite os dias alugados: '))
v_km = 0.15 * km
v_dia = 60 * dias
total = v_dia + v_km
print(f'Valor a pagar por R${total}')
