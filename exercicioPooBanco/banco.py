"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco
tem clientes e contas.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
"""
from cliente import *
from conta import *


class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.cliente = []
        self.conta = []

    def adicionar_cliente(self, cliente):
        self.cliente.append(cliente)

    def adicionar_conta(self, conta):
        self.conta.append(conta)

    def listar_clientes(self):
        for cliente in self.cliente:
            print(cliente.nome, cliente.idade, cliente.conta.numero_da_conta, cliente.conta.agencia)

    def autenticar(self, cliente):
        if cliente not in self.cliente:
            return False
        if cliente.conta not in self.conta:
            return False
        if cliente.conta.agencia not in self.agencias:
            return False
        return True
