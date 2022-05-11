frase = 'Amanda ama Pedro'.strip().lower()

print(frase)
print(f'A letra A aparece {frase.count("a")} vezes na frase.')
print(f'A primeira letra A aparece na posição: {frase.find("a")+1}')
print(f'A última letra A aparece na posição: {frase.rfind("a")+1}')


