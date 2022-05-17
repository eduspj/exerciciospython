matriz = []

while True:
    nome = (str(input('Nome: ')))
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    media = (nota1 + nota2) / 2
    matriz.append([nome, [nota1, nota2], media])
    continuar = input('Quer continuar? [S/N]: ')
    if continuar in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10} {"MÉDIA":>8}')
print('-' * 26)
for x, y in enumerate(matriz):
    print(f'{x:<4}{y[0]:<10}{(y[2]):>8}')
while True:
    print('-' * 50)
    aluno = int(input('Mostrar nota de qual aluno? [999 FIM]: '))
    if aluno == 999:
        print('FIM')
        break
    else:
        print(f'Notas de {matriz[aluno][0]} são {matriz[aluno][1]}')
