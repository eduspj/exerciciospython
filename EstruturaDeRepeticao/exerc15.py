# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.

n = 10
fib = 0
aux = 0
a = 1
b = 1

print(a, end=", ")
print(b, end=", ")
for x in range(0, n):
   fib = a + b
   b = a
   a = fib

   print(fib, end=", ")

