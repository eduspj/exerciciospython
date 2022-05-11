distancia = float(input('Digite a distância da viajem: '))
if distancia <= 200:
    print(f'O custo da passagem para viajem de {distancia}km é de {distancia * 0.50}')
else:
    print(f'O custo da passagem para viajem de {distancia}km é de {distancia * 0.45}')
    