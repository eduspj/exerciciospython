"""
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""


class Quadrado:
    def __init__(self, tamanho=0):
        self.tamanho = tamanho

    def mudar_valor_do_lado(self, tamanho):
        self.tamanho = tamanho

    def calcular_area(self):
        x = self.tamanho
        return x ** 2

    def retornar_valor_do_lado(self):
        print(self.tamanho)
        return self.tamanho


if __name__ == '__main__':
    q = Quadrado(10)
    q.retornar_valor_do_lado()
    q.mudar_valor_do_lado(15)
    q.retornar_valor_do_lado()
    print(q.calcular_area())

