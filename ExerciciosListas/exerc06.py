# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima
# o número de alunos com média maior ou igual a 7.0.

vetor_aluno = []
alunos = []

for a in range(1, 3):
    print('-' * 30)
    alunos = [input(f'Nome do {a}º aluno: ')]
    print('-' * 30)
    for b in range(1, 5):
        alunos.append(int(input(f'Nota {b} do {a}º aluno: ')))
    vetor_aluno.append(alunos)

print(vetor_aluno)

