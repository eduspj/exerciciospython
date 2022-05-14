n = int(input('Digite um nº para calcular o fatorial: '))
soma = 0
aux = n
while n != 1:
    soma = aux * (n - 1)
    aux = soma
    n -= 1

print(soma)
