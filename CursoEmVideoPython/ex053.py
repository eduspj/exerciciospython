frase = str(input('Digite uma frase: ')).strip().upper()

normal = frase.replace(' ', '')
inverso = normal[::-1]

if normal == inverso:
    print('É Palíndromo')
else:
    print('Não é Palíndromo')

print(normal)
print(inverso)
