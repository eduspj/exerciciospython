from random import randint


def jogada(opc):
    if opc == 0:
        return 'PEDRA'
    elif opc == 1:
        return 'PAPEL'
    elif opc == 2:
        return 'TESOURA'


print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURO')

jogador = int(input('Digite a jogada: '))
computador = randint(0, 2)
resultado = ' '
print(computador)
if jogador == 0 and computador == 0 or jogador == 0 and computador == 0 or jogador == 0 and computador == 0:
      resultado = 'DEU EMPATE'
elif jogador == 0 and computador == 2 or jogador == 1 and computador == 0 or jogador == 2 and computador == 1:
      resultado = 'JOGADOR VENCEU'
else:
      resultado = 'COMPUTADOR VENCEU'
print('-=' * 30)
print(f'Computador jogou {jogada(computador)}')
print(f'Jodador jogou {jogada(jogador)}')
print('-=' * 30)
print(resultado)
