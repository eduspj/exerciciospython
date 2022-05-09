# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero
# ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

x = int(input(('Qual tabuada? ')))

print(f'Tabuada do número {x}')
for a in range(1, 11):
    print(f'{x} x {a} = {x * a}')