num = int(input('Digite um número para converter: '))
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
opc = int(input('Digite a opção: '))
if opc == 1:
    print(bin(num)[2:])
elif opc == 2:
    print(oct(num)[2:])
elif opc == 3:
    print(hex(num)[2:])
