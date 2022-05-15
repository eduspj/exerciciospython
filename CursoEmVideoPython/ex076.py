listagem = ('Lápis', 1.50,
            'Caneta', 1.80,
            'Caderno', 4.80,
            'Agenda', 6.89,
            'Pasta', 2.70)

print('-' * 40)
print(f'{"Listagem de preços":^40}')
print('-' * 40)
for i, j in enumerate(listagem):
    if i % 2 == 0:
        print(f'{j:.<30} ', end='R$')
    else:
        print(f'{j:>7.2f}')
print('-' * 40)
