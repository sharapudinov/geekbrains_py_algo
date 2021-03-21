#7. Определить, является ли год, который ввел пользователь, високосным или не високосным.

year= int(input('year = '))

print('нет' if year%4 or year%400 or year%4 and not year%100 else 'да')

