# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = str(input('Digite o nome: '))
idade = str(input('Digite a idade: '))
salario = float(input('Digite o salario: '))
sexo = str(input('Digite o sexo "f" ou "m": '))
estado_civil = str(input("Digite o estado civil 's', 'c', 'v', 'd': "))

while len(nome) < 3:
    print('Nome tem de ter mais de 3 caracteres!!')
    nome = str(input('Digite o nome: '))
while not idade.isnumeric():
    print('Idade tem de ser número inteiro: ')
    idade = str(input('Digite a idade: '))
while salario < 0:
    print('Salário tem de ser maior que 0. ')
    salario = float(input('Digite o salario: '))
while sexo not in 'FfMm':
    sexo = str(input('Digite o sexo "f" ou "m": '))
while estado_civil not in 'SsCcVvDd':
    estado_civil = str(input("Digite o estado civil 's', 'c', 'v', 'd': "))

print()
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Salário: {salario}')
print(f'Sexo: {sexo}')
print(f'Estado civil: {estado_civil}')