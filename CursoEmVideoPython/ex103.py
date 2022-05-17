def ficha(nome='<desconhecido>', gols=0):
    return print(f'O jogador {nome} fez {gols} gols no campeonato!')


n = input('Nome: ')
g = input('Gols: ')

ficha(n, g)
