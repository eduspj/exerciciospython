import math
angulo = float(input('Digite o ângulo que vocÊ deseja: '))
seno = math.sin(math.radians(angulo))
print(f'O ângulo de {angulo} tem o seno de {seno:.2f}')
cosseno = math.cos(math.radians(angulo))
print(f'O ângulo de {angulo} tem o cosseno de {cosseno:.2f}')
tangente = math.tan(math.radians(angulo))
print(f'O ângulo de {angulo} tem o tangente de {tangente:.2f}')
