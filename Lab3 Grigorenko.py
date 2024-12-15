# Лаб работа №3
# Григоренко Анатолий, 100502-УБТа-о23, Вариант 7

# С помощью цикла for
import math
x1 = 2
xn = 8
dx = 0.7
a = 4.2
b = 1.5
per = int((xn - x1) / dx)

results = []

for x in range(per):
    x = x1 + x * dx
    y = (1 + a * x + b * math.cos(x)) ** (1/2)
    results.append((x, y))

for x, y in results:
    print(f"x = {x:.2f}, y = {y:.4f}")

# С помощью цикла while
import math

x1 = 2
xn = 8
dx = 0.7
a = 4.2
b = 1.5

results = []

x = x1
while x <= xn:
    y = (1 + a * x + b * math.cos(x)) ** (1/2)
    results.append((x, y))
    x += dx

for x, y in results:
    print(f"x = {x:.1f}, y = {y:.4f}")