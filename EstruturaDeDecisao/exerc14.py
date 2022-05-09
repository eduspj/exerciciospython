# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
media = (nota1 + nota2) / 2
conceito = ''
situação = ''

if 0 <= media < 4:
    conceito = 'E'
elif 4 <= media < 6:
    conceito = 'D'
elif 6 <= media < 7.5:
    conceito = 'C'
elif 7.5 <= media < 9:
    conceito = 'B'
elif 9 <= media <= 10:
    conceito = 'A'

if conceito in 'ABC':
    situação = 'APROVADO!!'
else:
    situação = 'REPROVADO'


print(f'Aluno tirou nas provas {nota1, nota2} e ficou com média {media}, CONCEITO: {conceito}')
print(situação)
