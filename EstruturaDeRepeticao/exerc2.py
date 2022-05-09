# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma
# mensagem de erro e voltando a pedir as informações.

nome_usuario = str(input('Digite o nome de usuário: '))
senha = str(input('Digite a senha: '))

while nome_usuario == senha:
    print()
    print('Senha não pode ser igual ao nome de usuário')
    print()
    nome_usuario = str(input('Digite o nome de usuário: '))
    senha = str(input('Digite a senha: '))

print(nome_usuario)
print(senha)