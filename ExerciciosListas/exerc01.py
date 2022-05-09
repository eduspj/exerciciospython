# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

vetor = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i, b in enumerate(vetor):
    print(i, b)

vetor.sort(reverse=True)
print()
print(vetor)
