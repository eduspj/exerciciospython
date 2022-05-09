# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino
# ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = str(input('Em qual turno vc estuda? (M-matutino ou V-Vespertino ou N- Noturno): '))

if turno not in 'MmVvNn':
    print('Valor inválido')
elif turno in 'Mm':
    print('Bom dia')
elif turno in 'Vv':
    print('Boa tarde')
elif turno in 'Nn':
    print('Boa noite')
