# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
# população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
# número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

continuar = False

while not continuar:
    pais_a = int(input('Digite a população do país A: '))
    pais_b = int(input('Digite a população do país B: '))
    pais_a_tx = float(input('Digite a taxa de crecimento do país A (%)')) / 100
    pais_b_tx = float(input('Digite a taxa de crecimento do país B (%)')) / 100
    anos = 0
    while pais_a <= pais_b:
        anos += 1
        pais_a = pais_a + (pais_a * pais_a_tx)
        pais_b = pais_b + (pais_b * pais_b_tx)
    print()
    print('=' * 30)
    print(pais_a)
    print(pais_b)
    print(anos)
    print('=' * 30)
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = input('Quer continuar(s/n)? ')
        if opcao in 'Nn':
            continuar = True
