palavras = ('Viajar', 'Elegante', 'Animal', 'Carro', 'Brasileiro', 'Abacate')

for i in palavras:
    print(f'Na palavra {i} temos as vogais: ', end=' ')
    for j in range(0, len(i)):
        if i[j] in 'aeiouAEIOU':
            print(i[j], end=' ')
    print()
