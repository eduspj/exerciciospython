def fatorial(num, show=False):
    aux = 1
    for i in range(num, 0, -1):
        aux *= i
        if show:
            print(i, end='')
            if i > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')

    return aux


print(fatorial(5, show=True))
