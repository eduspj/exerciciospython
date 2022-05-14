from random import randint

print('Vou pensar em um número entre 0 e 10 tente adivinhar...')
sorteio = randint(0, 10)
n = int(input('Em que número eu pensei? '))
cont = 1
while sorteio != n:
    n = int(input('Tente mais uma vez. Em que número eu pensei? '))
    cont += 1

print(f'Parabéns vc ganhou! escolhi o número {sorteio}, fez {cont} jogadas')
