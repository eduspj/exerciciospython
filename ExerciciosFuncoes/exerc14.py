"""
Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a
soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima.
Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado.
Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.
"""

import random
                #j(coluna)
matriz = [[1, 2, 3],#i(linha)
          [4, 5, 6],
          [7, 8, 9]]
res = False
#DEFINIR UMA FUNÇÃO PARA CALCULAR AS SOMAS DE TODOS OS LADOS
def magicsquare():
    if matriz[0][0] + matriz[1][0] + matriz[2][0] == matriz[0][1] + matriz[1][1] + matriz[2][1] == matriz[0][2] + matriz[1][2] + matriz[2][2] == matriz[0][0] + matriz[0][1] + matriz[0][2] == matriz[1][0] + matriz[1][1] + matriz[1][2] == matriz[2][0] + matriz[2][1] + matriz[2][2] == matriz[0][0] + matriz[1][1] + matriz[2][2] == matriz[0][2] + matriz[1][1] + matriz[2][0]:
        return res == True
    else:
        return res == False

#DEFINIR UM LOOP PARA GERAR Nº ALEAT. ATÉ ENCONTRAR OS QUE SATIZFAZEM
#AS CONDIÇÕES DE UM QUADRADO MÁGICO
seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while res == False:
    for i in range(2):
        for j in range(2):
            z = random.choice(seq)
            matriz[i][j] = z
            x = seq.index(z)
            seq[x] = []
    magicsquare()
print(matriz)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
res = False


def magicsquare():
    if vetor[0] + vetor[1] + vetor[2] == vetor[3] + vetor[4] + vetor[5] == vetor[6] + vetor[7] + vetor[8] == vetor[0] + vetor[3] + vetor[6] == vetor[1] + vetor[4] + vetor[7] == vetor[2] + vetor[5] + vetor[8] == vetor[0] + vetor[4] + vetor[8] == vetor[2] + vetor[4] + vetor[6]:
        return res == True
    else:
        return res == False
#        0  1  2  3  4  5  6  7  8
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9]
seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
if res == False:
    for i in range(8):
        w = random.choice(seq)
        #Repor o valor w(1 a 9) no index i(0 a 8). Sem usar valores e indexes repetidos
        vetor.insert(i, w)
        #Eliminar os valores já utilizados
        x = seq.index(w)
        seq[x] =[]
    magicsquare()
print(vetor)