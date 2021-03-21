#5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

pos_a =int(input('position of letter = '))

print(chr(pos_a+ord('A')-1))
