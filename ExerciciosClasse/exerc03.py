"""
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois,
deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""


class Retangulo:
    def __init__(self, b, a):
        self.base = int(b)
        self.altura = int(a)

    def mudar_valor_dos_lados(self):
        b = input('Digite a nova base: ')
        a = input('Digite a nova altura: ')
        self.base = int(b)
        self.altura = int(a)

    def retornar_valor_dos_lados(self):
        print(f'Base = {self.base}, Altura = {self.altura}')
        return self.base, self.altura

    def calcular_area(self):
        area = int(self.base) * int(self.altura)
        print(f'A área do retângulo é {area}')
        return area

    def calcular_perimetro(self):
        perimetro = self.base * 2 + self.altura * 2
        print(f'O perímetro é {perimetro}')
        return perimetro


if __name__ == '__main__':
    base = input('Digite a base do retângulo: ')
    altura = input('Digite a altura do retângulo: ')

    local = Retangulo(base, altura)
    piso = Retangulo(1, 2)
    rodape = Retangulo(2, 3)

    pisos_necessarios = local.calcular_area() / piso.calcular_area()
    rodapes_necessarios = local.calcular_perimetro() / rodape.base
    print(f'São necessários {pisos_necessarios} pisos')
    print(f'São necessários {rodapes_necessarios} rodapés')
