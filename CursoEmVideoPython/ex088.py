from random import randint

jogos = []
aux = []
qtd = int(input('Quantos jogos quer jogar? '))
for i in range(1, qtd+1):
    for j in range(0, 6):
        while True:
            numero = randint(1, 60)
            if numero not in aux:
                aux.append(numero)
                break
    aux.sort()
    jogos.append(aux[:])
    print(f'Jogo {i}: {aux}')
    aux.clear()
print('-' * 30)
for i, j in enumerate(jogos):
    print(i, j)
