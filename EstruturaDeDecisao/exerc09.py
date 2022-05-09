# Faça um Programa que leia três números e mostre-os em ordem decrescente.

a = 11
b = 9
c = 10

if a >= b >= c and a >= c:
    print(c, b, a)
elif c <= a <= b:
    print(c, a, b)
elif b <= a <= c and b <= c:
    print(b, a, c)
elif b <= c <= a:
    print(b, c, a)
elif a <= b <= c:
    print(a, b, c)
elif a <= c <= b:
    print(a, c, b)

# aux1 = 0
# aux2 = 0
# aux3 = 0
#
# if a > b:
#     if a > c:
#         aux1 = a
#         if b > c:
#             aux2 = b
#             aux3 = c
#         else:
#             aux2 = c
#             aux3 = b
#     else:
#         aux1 = c
#         aux2 = a
#         aux3 = b
# else:
#     if b > c:
#         aux1 = b
#         if c > a:
#             aux2 = c
#             aux3 = a
#         else:
#             aux2 = a
#             aux3 = c
#     else:
#         aux1 = c
#         aux2 = b
#         aux3 = a
#
# print(f'Ordem dos numeros decrescentes {aux1, aux2, aux3}')