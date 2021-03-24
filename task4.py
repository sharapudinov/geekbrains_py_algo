# 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

# тривиальный алгоритм, блоксхема не нужна

a = input('a = ')

pos_a = ord(a) - ord('A') if ord('A') <= ord(a) <= ord('Z') else ord(a) - ord('a')

b = input('b = ')

pos_b = ord(b) - ord('A') if ord('A') < ord(b) < ord('Z') else ord(b) - ord('a')

print(pos_a, pos_b, abs(pos_a - pos_b) - 1)
