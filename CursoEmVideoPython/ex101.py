from datetime import date


def voto(ano):
    idade = date.today().year - ano
    if 16 <= idade < 18 or idade >= 60:
        return 'OPCIONAL'
    elif idade < 16:
        return 'NEGADO'
    elif 18 <= idade < 60:
        return 'OBRIGATÓRIO'


nasc = 1956
voto = voto(nasc)
print(f' Tem {date.today().year - nasc} anos e o voto é {voto}')
