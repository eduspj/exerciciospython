"""
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir
os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes:
 alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais
 atributos são obrigatórios.
"""


class ContaCorrente:
    def __init__(self, numero_da_conta, nome_do_correntista, saldo=0):
        self.numero_da_conta = numero_da_conta
        self.nome_do_correntista = nome_do_correntista
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome_do_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor


if __name__ == '__main__':
    a = ContaCorrente(1, 'Edu')
    print(a.numero_da_conta, a.nome_do_correntista, a.saldo)
    a.alterar_nome('Elisa')
    print(a.numero_da_conta, a.nome_do_correntista, a.saldo)
    a.deposito(15)
    print(a.numero_da_conta, a.nome_do_correntista, a.saldo)
    a.saque(8)
    print(a.numero_da_conta, a.nome_do_correntista, a.saldo)
