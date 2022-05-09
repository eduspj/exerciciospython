"""
Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores
deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""

vetor1 = []
vetor2 = []
vetor_intercalado = []

for a in range(1, 3):
    vetor1.append(input(f'Digite um valor: '))
for b in range(1, 3):
    vetor2.append(input(f'Digite um valor: '))
for c in range(0, 2):
    vetor_intercalado.append(vetor1[c])
    vetor_intercalado.append(vetor2[c])

print(vetor1)
print(vetor2)
print(vetor_intercalado)
