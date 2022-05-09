# Faça um Programa que leia três números e mostre o maior e o menor deles.

a = 10
b = 12
c = 9

maior = 0
menor = a

if a > b:
    menor = b
    if a > c:
        if c < b:
            menor = c
        maior = a
    else:
        maior = c
else:
    if b > c:
        maior = b
        if c < a:
            menor = c
    else:
        maior = c

print(maior)
print(menor)
