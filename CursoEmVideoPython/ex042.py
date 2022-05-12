def eh_triangulo(a, b, c):
    if ((b - c) < a < (b + c)) and (a - c) < b < (a + c) and ((a - b) < c < (a + b)):
        return True
    else:
        return False


lado1 = float(input('Digite o lado A: '))
lado2 = float(input('Digite o lado B: '))
lado3 = float(input('Digite o lado C: '))

if eh_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        print(f'Lados iguais, triângulo EQUILÂTERO')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Dois lador iguais, triângulo ISÓSCELES')
    else:
        print('Lados diferentes, triângulo ESCALENO')
else:
    print('Não é triângulo')
