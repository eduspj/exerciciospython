"""
Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13
anos possuem altura inferior à média de altura desses alunos.
"""

import random

idade = []
altura = []
media_altura = 0.0
contador = 0

for a in range(0, 30):
    idade.append(random.randint(5, 18))
    altura.append(round(random.uniform(1.20, 1.90), 2))
    media_altura += float(altura[a])

media_altura = round(media_altura / 30, 2)

for b in range(0, 30):
    print(f'[{idade[b]}, {altura[b]}]', end=" ")
    if idade[b] > 13 and altura[b] < media_altura:
        contador += 1

print()
print(media_altura)
print(f'{contador} alunos com mais de 13 anos estão abaixo da média de altura {media_altura}')