primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
aux = primeiro_termo

for i in range(0, 10):
    if i == 0:
        print(f'{primeiro_termo} -> ', end='')
    else:
        aux += razao
        print(f'{aux} -> ', end='')
print("ACABOU")