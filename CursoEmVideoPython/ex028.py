from random import randint

print('Vou pensar em um número entre 0 e 5 tente adivinhar...')
sorteio = randint(0, 5)
n = int(input('Em que número eu pensei? '))
if sorteio == n:
    print(f'Parabéns vc ganhou! escolhi o número {sorteio}')
else:
    print(f'Ganhei, escolhi o número {sorteio}')

