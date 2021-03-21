# . Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = float(input('a ='))
b = float(input('b ='))
c = float(input('c ='))

print(a + b + c - max(a, b, c) - min(a, b, c))
