"""
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
"""

vetor = []
num = 0

for a in range(1, 3):
    num = int(input(f'Digite um número: '))
    vetor.append(num ** 2)

print(vetor)