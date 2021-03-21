# 2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
# блоксхема https://drive.google.com/file/d/1qM5yZatZ0WHHBzluk14gAaL1AKJvxGDE/view?usp=sharing

x1 = float(input('x1='))
y1 = float(input('y1='))
x2 = float(input('x2='))

if x2 == x1:  # y2 можно уже не спрашивать
    print(f'x = {x1}')

else:
    y2 = float(input('y2='))
    k = (y2 - y1) / (x2 - x1)
    print(f'y = {"x + " if k == 1 else "" if k == 0 else f"{k}x + "}{y1 - k * x1}')
