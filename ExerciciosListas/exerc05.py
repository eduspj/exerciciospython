# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e
# os números IMPARES no vetor impar. Imprima os três vetores.

vetor = []
par = []
impar = []

for a in range(1, 21):
    vetor.append(int(input(f' Digite o {a}º número: ')))

for i, v in enumerate(vetor):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(vetor)
print(par)
print(impar)
