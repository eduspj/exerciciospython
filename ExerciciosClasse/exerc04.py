"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a
 idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        if self.idade < 21:
            self.idade += 1
            self.altura += 0.05
        else:
            self.idade += 1

    def engordar(self, peso_que_engordou):
        self.peso += peso_que_engordou

    def emagrecer(self, peso_que_emagreceu):
        self.peso -= peso_que_emagreceu

    def crescer(self, quanto_cresceu):
        self.altura += quanto_cresceu


if __name__ == '__main__':
    x = Pessoa('Edu', 18, 71.5, 1.80)
    print(x.idade)
    print(x.altura)
    x.envelhecer()
    print(x.idade)
    print(x.altura)
    x.engordar(3)
    print(x.peso)
    x.emagrecer(2)
    print(x.peso)
    x.crescer(5)
    print(x.altura)