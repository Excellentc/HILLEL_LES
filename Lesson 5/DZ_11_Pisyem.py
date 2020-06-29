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
    for i in range(x):
        for j in range(x):
            if inp == 3:                            # ромб простой
                if (
                        i == j + x // 2
                        or i == j - x // 2
                        or j - x // 2 == x - i - 1
                        or j + x // 2 == x - i - 1
                        or x // 2 + i >= j >= x // 2 - i and i <= x // 2
                        # or j == x // 2 and x % 2 == 0
                        # or j == x // 2 - 1 and x % 2 == 0
                        # or j == x // 2 and x % 2 == 1
                ):
                    print("*  ", end="")
                else:
                    print("   ", end="")
            elif inp == 4:                           # ромб с палочкой
                if (
                        i == j + x // 2
                        or i == j - x // 2
                        or j - x // 2 == x - i - 1
                        or j + x // 2 == x - i - 1
                        or x // 2 + i >= j >= x // 2 - i and i <= x // 2
                        or j == x // 2 and x % 2 == 0
                        or j == x // 2 - 1 and x % 2 == 0
                        or j == x // 2 and x % 2 == 1
                ):
                    print("*  ", end="")
                else:
                    print("   ", end="")
        print()
    print()
