while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    if tabuada < 0:
        break
    for i in range(1, 11):
        print(f'{tabuada} x {i} = {tabuada * i}')
