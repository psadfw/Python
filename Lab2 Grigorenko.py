# Лаб работа №2
# Григоренко Анатолий, 100502-УБТа-о23, Вариант 7

import math
import sys

x = float(input('Введите значение х: '))
y = float(input('Введите значение y: '))

f = float(input('Выберите функцию (номер): \n1) tgh(y) \n2) 2^y \n3) sh(x/y) \n'))
c = None

match f:
    case 1:
        f = math.tanh(y)
    case 2:
        f = 2 ** y
    case 3:
        f = math.sinh(x / y)
    case _:
        print('Некорректный выбор функции')
        sys.exit()

if 1 < x * y < 10:
    c = math.exp(f)
elif 0.1 < x * y < 0.5:
    c = (abs(f + 4 * y)) ** (1/3)
else:
    c = y * (f ** 2)

print('Результат: ', c)