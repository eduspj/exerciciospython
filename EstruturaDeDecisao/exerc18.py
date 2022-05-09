# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = str(input('Digite uma data (dd/mm/aaaa): '))
dia = int(data[0] + data[1])
mes = int(data[3] + data[4])
ano = int(data[6] + data[7] + data[8] + data[9])

if data[2] == '/' and data[5] == '/':
    if 0 < dia <= 31:
        if 0 < mes <= 12:
            if 0000 < ano < 9999:
                print(f'{dia}/{mes}/{ano}')
            else:
                print('Ano inválido')
        else:
            print('Mês inválido')
    else:
        print('Dia inválido')
else:
    print('DAta inválida')