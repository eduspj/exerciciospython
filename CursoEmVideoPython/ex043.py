peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = peso / (altura ** 2)
print(imc)
if 18.5 < imc < 25:
    print(f'{imc}: Peso ideal')
elif imc < 18.5:
    print(f'{imc}: Abaixo do peso.')
elif 25 < imc <= 30:
    print(f'{imc}: Sobrepeso')
elif 30 < imc <= 40:
    print(f'{imc}: Obesidade')
elif imc > 40:
    print(f'{imc}: Obesidade mórbida')
