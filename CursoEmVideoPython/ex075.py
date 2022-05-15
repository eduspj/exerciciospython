tupla = (int(input('Digite 1º valor: ')), int(input('Digite 2º valor: '))
         , int(input('Digite 3º valor: ')), int(input('Digite 4º valor: ')))
print(f'Apareceu o 9 em {tupla.count(9)} lugares')
print(f'O primeiro valor 3 é na posição {tupla.index(3)}')
for i in tupla:
    if i % 2 == 0:
        print(i)
