valor = int(input('Quer sacar qual valor? R$ '))
total = valor
ced50 = 0
ced20 = 0
ced10 = 0
ced1 = 0
while True:
    if total >= 50:
        total -= 50
        ced50 += 1
    else:
        if total >= 20:
            total -= 20
            ced20 += 1
        else:
            if total >= 10:
                total -= 10
                ced10 += 1
            else:
                if total >= 1:
                    total -= 1
                    ced1 += 1
                else:
                    break3
print(ced50)
print(ced20)
print(ced10)
print(ced1)
