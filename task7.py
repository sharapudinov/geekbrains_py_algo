# блоксхемы я не рисую из принципа. курс называется алгоритмы на языке питон  а не уроки рисования.

# 7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

while True:
    n = int(input('n = '))
    if n == 0:
        break
    s = 0;
    for i in range(n):
        s += i

    print(f'{"не" if s != (n * n - n) / 2 else ""} выполняется')
