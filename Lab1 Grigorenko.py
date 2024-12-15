# Лаб работа №1
# Григоренко Анатолий, 100502-УБТа-о23, Вариант 7

import math
x = float(input("Введите значение x -> "))
y = float(input("Введите значение y -> "))
z = float(input("Введите значение z -> "))

if (abs(x - y)) * z == 0 or abs(x) >= 1:
    print('Значение выражения не может быть вычислено')

else:
    a = 5 * math.atan(x)
    b = 1/4 * math.acos(x)
    c = (abs(x - y) + x**2) / (abs(x-y) * z)
    s = a - b * c
    print('Результат: ', s)