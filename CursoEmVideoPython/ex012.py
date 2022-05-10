preco = float(input('Digite o preço: R$'))
desconto = float(input('Digite a porcentagem do desconto: '))
novo_preco = preco - (preco * desconto / 100)
print(f'Preço com desconto R${novo_preco}')
