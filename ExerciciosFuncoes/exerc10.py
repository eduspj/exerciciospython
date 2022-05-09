"""
Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor
entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na
primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,
este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no
entanto, se tirar um 7 antes de tirar este Ponto novamente.
"""
import random


def dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    print(f'Dado1 = {dado1} / Dado2 = {dado2} / TOTAL = {dado1 + dado2}')
    return dado1 + dado2


ponto = 0
jogadas = 0
valor = 0
continuar = True
while continuar:
    print('-' * 30)
    input('Gire o dado:')
    valor = dados()
    jogadas += 1
    if jogadas == 1:
        ponto = valor
        if valor == 7 or valor == 11:
            print(f'NATURAL, tirou {valor} na 1º jogada')
            continuar = False
        elif valor == 2 or valor == 3 or valor == 12:
            print(f'CRAPS, tirou {valor} na 1º jogada')
    else:
        if valor == 7:
            print(f'Você perdeu, tirou {valor}')
            continuar = False
        elif valor == ponto:
            print(f'GANHOU!! Seu ponto é {ponto}, você tirou {valor}')
            continuar = False


