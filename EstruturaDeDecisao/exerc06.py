# Faça um Programa que leia três números e mostre o maior deles.

a = 9
b = 7
c = 11

aux = 0

if a > b:
    if a > c:
        aux = a
    else:
        aux = c
else:
    if b > c:
        aux = b
    else:
        aux = c

maior = max(a, b, c)

print(maior)
print(aux)
