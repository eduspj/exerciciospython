"""
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a
média anual das temperaturas e mostre todas as temperaturas acima da média anual,
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""
import random

mes = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
temp_media = []
media_anual = 0.0

for a in range(0, 12):
    temp_media.append(round(random.uniform(0.0, 44.0), 2))
    media_anual += temp_media[a]

media_anual = round(media_anual / 12, 2)

for b in range(0, 12):
    if temp_media[b] > media_anual:
        print(f'{mes[b]} = {temp_media[b]} ficou acima da média anual de {media_anual} ')

print()
print(mes)
print(temp_media)
print(media_anual)