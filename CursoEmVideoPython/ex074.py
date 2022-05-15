from random import randint

sorteio = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(sorteio)
print(f'Maior {max(sorteio)}')
print(f'Menor {min(sorteio)}')
