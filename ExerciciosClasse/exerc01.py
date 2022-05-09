"""
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
    >>> bola = Bola('Branco', 15, 'ferro')

"""


class Bola:
    def __init__(self, cor='ND', circunferencia=0, material='ND'):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, cor):
        self.cor = cor

    def mostra_cor(self):
        return print(self.cor)


if __name__ == '__main__':
    b = Bola('Branco', 15, 'ferro')
    print(b.cor)
    b.troca_cor('Cinza')
    print(b.cor)
    b.mostra_cor()
