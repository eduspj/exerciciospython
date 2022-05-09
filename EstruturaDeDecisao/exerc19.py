# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
# dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

num = int(input('Digite um número inteiro: '))
resposta_centena = str('')
resposta_dezena = str('')
resposta_unidade = str('')

centena = ''
dezena = ''
unidade = ''

if num >= 1000 or num < 0:
    print('numero inválido')
else:
    if num > 99:
        num2 = str(num)
        centena = int(num2[0])
        dezena = int(num2[1])
        unidade = int(num2[2])

        if centena == 1:
            resposta_centena = 'centena, '
        else:
            resposta_centena = 'centenas, '
        if dezena == 1:
            resposta_dezena = 'dezena e '
        else:
            resposta_dezena = 'dezenas e '
        if unidade == 1:
            resposta_unidade = 'unidade.'
        else:
            resposta_unidade = 'unidades.'
    elif 9 < num <= 99:
        num2 = str(num)
        dezena = int(num2[0])
        unidade = int(num2[1])

        if dezena == 1:
            resposta_dezena = 'dezena e '
        else:
            resposta_dezena = 'dezenas e '
        if unidade == 1:
            resposta_unidade = 'unidade.'
        else:
            resposta_unidade = 'unidades.'

    elif 0 <= num <= 9:
        num2 = str(num)
        unidade = int(num2[0])
        if unidade == 1:
            resposta_unidade = 'unidade.'
        else:
            resposta_unidade = 'unidades.'

print(f'{num} = {centena} {resposta_centena} {dezena} {resposta_dezena} {unidade} {resposta_unidade} ')

# #Pedindo valor
# valor=int(input('Dgite um valor: '))
#
# #Comparando se valor é menor que 1000
# if(valor <= 1000):
# #Calculos
# uni=valor % 10
# dez=valor/10 % 10
# cent=valor/100 % 100
# #Comparando valor
# print('Neste número a %d centenas, %d dezenas e %d unidades'%(cent,dez,uni))
# else:
# print('Infelizmente o número %d é maior que mil'%valor)
