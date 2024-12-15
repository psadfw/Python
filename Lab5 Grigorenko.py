# Лаб работа №5
# Григоренко Анатолий, 100502-УБТа-о23, Вариант 7

# Задание 1
import math

numbers = input('Введите целые числа через пробел: ', ).split()
numbers = [int(num) for num in numbers]
nums1 = []
nums2 = []


for i in numbers:
    index = numbers.index(i)
    if index % 2 == 0:
        nums1.append(i)
    else:
        nums2.append(i)

one = sum(nums1)
two = math.prod(nums2)

print('Четные числа: ', one, '\nНечетные числа: ', two)

# Задание 2
numbers = input('Введите целые числа через пробел: ', ).split()
numbers = [num for num in numbers]

min_i = numbers.index(min(numbers))
max_i = numbers.index(max(numbers))

numbers[min_i], numbers[max_i] = numbers[max_i], numbers[min_i]

print(numbers)