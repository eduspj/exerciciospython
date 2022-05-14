nome_mais_velho = ''
idade_mais_velho = 0
media = 0
mulheres = 0

for i in range(1, 5):
    print(f'------ {i}ª PESSOA ------')
    nome = input('Nome: ')
    idade = float(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    media += idade
    if idade > idade_mais_velho and sexo == 'M':
        idade_mais_velho = idade
        nome_mais_velho = nome
    if sexo == 'F' and idade < 20:
        mulheres += 1

media = media / 4

print(f'A média de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {idade_mais_velho} e se chama {nome_mais_velho}.')
print(f'Ao todo sao {mulheres} mulheres com menos de 20 amos.')
