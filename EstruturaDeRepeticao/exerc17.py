# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120


continuar = False
while not continuar:
    fatorial = int(input('Digite um número: '))
    soma = fatorial
    print(fatorial, end="*")
    for a in range(fatorial - 1, 0, -1):
        soma = soma * a
        if a == 1:
            print(a, end="=")
        else:
            print(a, end="*")
    print(soma)
    aux = ' '
    while aux not in 'SsNn':
        aux = input('Quer continuar? s/n: ')
        if aux in 'Nn':
            continuar = True
