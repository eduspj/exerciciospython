x = str(input('Digite o seu nome completo: ')).strip().upper()

print(f'Seu nome tem Silva? {x.count("SILVA") == 1}')
# Outra forma
print(f'Seu nome tem Silva? {"SILVA" in x}')
