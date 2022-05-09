"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco
tem clientes e contas.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)                    =======> OK
    Pessoa tem nome e idade (com getters)                                    =======> OK
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)   =======> OK
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta             =======> OK
    ContaCorrente deve ter um limite extra                                  =======> OK
    Contas têm agência, número da conta e saldo                             =======> OK
    Contas devem ter método para depósito                                   =======> OK
    Conta (super classe) deve ter o método sacar abstrato (Abstração e      =======> OK
    polimorfismo - as subclasses que implementam o método sacar)            =======> OK
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
"""
from abc import ABC, abstractmethod  # classe abstrata


class Conta(ABC):
    def __init__(self, agencia, numero_da_conta, saldo=0):
        self.agencia = agencia
        self.numero_da_conta = numero_da_conta
        self.saldo = saldo

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor precisa ser numérico")
        self.saldo += valor

    def detalhes(self):
        print(f'Agência: {self.agencia}\n'
              f'Conta: {self.numero_da_conta}\n'
              f'Saldo: {self.saldo}')

    @abstractmethod  # Classe abstrata, exige das outras clases a criação do método seguinte
    def sacar(self, valor):
        pass

    # @property
    # def agencia(self):
    #     return self._agencia
    #
    # @property
    # def numero_da_conta(self):
    #     return self._numero_da_conta
    #
    # @property
    # def saldo(self):
    #     return self._saldo
    #
    # @saldo.setter
    # def saldo(self, valor):
    #     if not isinstance(valor, (int, float)):
    #         raise ValueError("Saldo precisa ser numérico")
    #     self._saldo = valor
    #     print(f'Saldo atual = {self._saldo}')


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=100):
        super().__init__(agencia, conta, saldo=0)
        self.limite = limite

    # @property
    # def limite(self):
    #     return self._limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print(f'Saldo insuficiente, saldo atual {self.saldo}')
            return
        self.saldo -= valor
        print(f'Saldo atual = {self.saldo}')
        self.detalhes()


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print(f'Saldo insuficiente, saldo atual = {self.saldo}')
            return
        self.saldo -= valor
        self.detalhes()
