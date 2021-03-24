# Написать программу, которая генерирует в указанных пользователем границах:
# структура кода линейна, сблоксхема бессмыслена

from random import randrange, uniform

a = int(input('a = '))
b = int(input('b = '))

print(randrange(a, b, 1))

x = float(input('x = '))
y = float(input('y = '))

print(uniform(x, y))

char_left = input('char_left = ')
char_right = input('char_right = ')

print(chr(randrange(ord(char_left[0]), ord(char_right[0]))))
