"""
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade
b. Métodos: Alterar Nome, Fome, Saúde e Idade;
Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o
Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo
calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada
 a qualquer momento.
"""


class BichinhoVirtual:
    fome = 0
    saude = 100
    idade = 0
    humor = 100

    def __init__(self, nome, ):
        self.nome = nome

