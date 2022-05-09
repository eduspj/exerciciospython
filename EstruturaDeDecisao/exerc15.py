# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores
# podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

a = float(input('Digite o Lado A: '))
b = float(input('Digite o Lado B: '))
c = float(input('Digite o lado C: '))

if (a + b) > c and (a + c) > b and (b + c) > a:
    if a == b == c:
        print(f'Triângulo Equilátero: três lados iguais: {a, b, c}')
    elif a == b or a ==c or b == c:
        print(f'Triângulo Isósceles: quaisquer dois lados iguais: {a, b, c}')
    else:
        print(f'Triângulo Escaleno: três lados diferentes: {a, b, c}')
else:
    print('Não é triângulo: ')