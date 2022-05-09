"""
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados
quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
"""

dados = []
aux = 0
confirmar = False
soma = 0
media = 0
acima_media = 0
abaixo7 = 0

while not confirmar:
    aux = int(input('Digite uma nota: '))
    if aux == -1:
        confirmar = True
        media = soma / len(dados)
    else:
        dados.append(aux)
        soma += aux

for a in range(0, len(dados)):
    if dados[a] > media:
        acima_media += 1
    if dados[a] < 7:
        abaixo7 += 1

print(f'A = {len(dados)} valores')
print(f'B = {dados}')
for a in range(len(dados)-1, -1, -1):
    print(f'C = {dados[a]}')
print(f'D = Soma dos valores = {soma} ')
print(f'E = Média dos valores = {media}')
print(f'F = Valores acima da média = {acima_media}')
print(f'G = Valores abaixo de sete = {abaixo7}')
print(f'FIM DO PROGRAMA')