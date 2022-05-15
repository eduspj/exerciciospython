tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
         'oito', 'nove', 'dez')
while True:
    num = int(input('Digite um número: '))
    if num <= 10:
        print(f'O número digitado é {tupla[num]}')
        break
