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
from banco import *

itau = Banco()

cliente1 = Cliente('Eduardo', 39)
cliente2 = Cliente('Maria', 25)
cliente3 = Cliente('João', 34)

conta1 = ContaPoupanca(1111, 254136)
conta2 = ContaCorrente(2222, 254148)
conta3 = ContaPoupanca(1119, 254149)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

itau.adicionar_conta(conta1)
itau.adicionar_cliente(cliente1)

itau.adicionar_conta(conta2)
itau.adicionar_cliente(cliente2)

print(itau.listar_clientes())


if itau.autenticar(cliente1):
    cliente1.conta.depositar(40)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado')

print('#######################')

if itau.autenticar(cliente2):
    cliente2.conta.depositar(40)
    cliente2.conta.sacar(20)
else:
    print('Cliente não autenticado')

# pessoa1 = Pessoa('Eduardo', 35)
# conta1 = ContaCorrente(1111, 3333)
# cliente1 = Cliente(pessoa1.nome, pessoa1.idade)
# cliente1.inserir_conta(conta1)
# print(cliente1.nome)
# print(cliente1.idade)
# print(cliente1.conta.numero_da_conta)
# print(cliente1.conta.agencia)
# b1 = Banco()
# b1.adicionar_conta(conta1)
# b1.adicionar_cliente(cliente1)
# print(b1.cliente)
# conta1.detalhes()

# p = Pessoa('Eduardo', 39)
# print(p.nome, p.idade)

# conta = ContaPoupanca(1111, 2222)
# print(f'numero da conta = {conta.numero_da_conta}')
# print(f'agência = {conta.agencia}')
# conta.depositar(520)
# conta.sacar(15)
# conta.sacar(15)
# conta.sacar(490)
# print('###################')
# cc = ContaCorrente(3333, 4444, saldo=0)
# cc.depositar(100)
# cc.depositar(120)
# cc.depositar(150)
# cc.depositar(190)
# cc.sacar(280)
# cc.sacar(280)
# cc.sacar(60)
