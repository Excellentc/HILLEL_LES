"""
При помощи вложенных циклов (можно while, можно for) нарисовать следующие фигуры
представленные ниже. Пользователь вводит, с клавиатуры, высоту фигуры в символах.

"""

x = int(input("Введите высоту фигуры : "))
inp = int(input("Нарисовать не закрашенный треугольник [Введите 1] : \n"
                "Нарисовать закрашенный треугольник [Введите 2] : \n"
                "Нарисовать ромб, вариант 1 [Введите 3] : \n"
                "Нарисовать ромб, вариант 2 [Введите 4] : "))
print()
if inp == 1 or inp == 2:
    print()
    for i in range(x):
        for j in range(x*2):
            if inp == 1:                            # треугольник пустой
                if (
                        j == x - i or j == x + i
                        or i == x - 1 and j != 0
                ):
                    print("*  ", end="")
                else:
                    print("   ", end="")
            elif inp == 2:                          # треугольник полный
                if x+i >= j >= x - i:
                    print("*  ", end="")
                else:
                    print("   ", end="")
        print()
    print()
elif inp == 3 or inp == 4:
    for i in range(x*2-1):
        for j in range(x*2):
            if inp == 3:  # ромб простой
                if (
                        x+i >= j >= x - i and i <= x - 1
                        or i - x + 2 == j > 0
                        or j + 1 == 2 * x - i + x - 1 and j < x * 2 - 1
                ):
                    print("*  ", end="")
                else:
                    print("   ", end="")
            elif inp == 4:  # ромб с палочкой
                if (
                        x+i >= j >= x-i and i <= x-1
                        or i - x + 2 == j > 0
                        or j + 1 == 2 * x - i + x - 1 and j < x * 2 - 1
                        or i >= x-2 and j == x
                ):
                    print("*  ", end="")
                else:
                    print("   ", end="")
        print()
    print()
