expressao = [input('Digite uma expressão: ')]

aberto = 0
fechado = 0
validar = True

print(expressao)
for i in expressao:
    for j in range(0, len(i)):
        if i[j] == '(':
            aberto += 1
        if i[j] == ')':
            if fechado < aberto:
                fechado += 1
            else:
                print('Expressão inválida')
                validar = False
                break
if validar:
    if aberto == fechado:
        print('Expressão Válida')


print(aberto)
print(fechado)
