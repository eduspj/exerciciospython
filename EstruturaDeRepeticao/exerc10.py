# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
soma = 0

for a in range(a+1, b):
    print(a)
    soma += a

print()
print(soma)
