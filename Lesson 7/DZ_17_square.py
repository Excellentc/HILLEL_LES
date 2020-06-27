"""
    Написать функцию square, принимающую 1 аргумент — сторону квадрата,
и возвращающую 3 значения (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
"""

# ПЕРВЫЙ ВАРИАНТ С ИСПОЛЬЗОВАНИЕМ БИБЛИОТЕКИ MATH
import math


def square(x1):
    return x1*4, x1*x1, math.sqrt(x1**2*2)


x = int(input("Введите длину стороны квадрата : "))
print()
print(square(x))

# ВТОРОЙ ВАРАИНТ БЕЗ БИБЛИОТЕКИ

# def square(x1):
#     return x1*4, x1*x1, (x1**2*2)**0.5
#
#
# x = int(input("Введите длину стороны квадрата : "))
# print()
# print(square(x))