from datetime import date

maiores = 0
menores = 0
data = date.today().year

for i in range(1, 8):
    aux = int(input(f'Ano de nascimento da {i}ª pessoa: '))
    if data - aux >= 18:
        maiores += 1
    else:
        menores += 1

print(f'Maiores {maiores}')
print(f'Menores{menores}')
