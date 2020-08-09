"""
    Написать функцию сортировки двухмерного списка МхМ (матрицы) Значение М - задаётся пользователем, с клавиатуры.
Может быть любымцелым, положительным числом, больше 5.
Функция должна:
    1. найти сумму элементов столбцов и отсортировать столбцы повозрастанию этих сумм
    2. отсортировать каждый нечётный столбец по возрастанию значений снизу вверх, а каждый чётный столбец по возрастанию
значений сверху вниз. Так же, ваша программа должна иметь функцию вывода данного спискана экран. При выводе, внизу каж
дого столбца должна выводиться суммаэлементов этого столбца.
    Что можно использовать:
    1. для создания списка использовать ТОЛЬКО 'list comprehension' и генератор случайных чисел. Диапазон случайных
чисел для заполнения списка от 1 до 50. Список должен создаваться однострочнымвыражением.
    2. Можно использовать ТОЛЬКО ДВА списка. Первый это двухмерный список размером МхМ, второй, вспомогательный, одно
мерный список размером М. Использование других списков (или коллекций) НЕДОПУСТИМО.
    3. Можно использовать ТОЛЬКО ОДНУ переменную М для хранения размера списка, плюс переменные циклов for.
    4. Для сортировки можно использовать алгоритм пузырьковой сортировки. Использование встроенных функций сортировки -
НЕДОПУСТИМО (да и неполучится их использовать)!
    5. Решение должно включать ТОЛЬКО ДВЕ функции: функцию сортировки (поправилам описанным выше) и функцию вывода на
экран.
Задача считается решённой верно при условии соблюдения всех требований.
Аккуратный вывод на экран - приветствуется.

"""

from random import randint as rand


def bubble_sort(l, n):
    for i in range(len(l) - 1):
        l1 = []
        for j in range(len(l) - 1):  # Отсеиваем столбик массива, в отдельный список
            l1.append(l[j][i])
        l[n][i] = sum(l1)
    # Пузырек по суммам столбцов
    for i in range(n - 1):
        fl = True
        for j in range(n - 1 - i):
            if l[n][j] > l[n][j + 1]:
                l[n][j], l[n][j + 1] = l[n][j + 1], l[n][j]  # Перебрасываем суммы столбцов
                for p in range(n):
                    l[p][j], l[p][j + 1] = l[p][j + 1], l[p][j]  # Перебрасываем столбики целиком
                fl = False
        if fl:
            break
    # Пузырек по столбцам
    for x in range(len(l) - 1):
        l1 = []
        for k in range(len(l) - 1):
            l1.append(l[k][x])

        for i in range(n - 2):
            fl = True
            for j in range(n - 1 - i):
                if l1[j] > l1[j + 1]:
                    l1[j], l1[j + 1] = l1[j + 1], l1[j]
                    fl = False
            if fl:
                break
        # Сортировка столбцов Чет/Нечет по Возростанию/Убыванию
        if x % 2 == 0:
            l1.reverse()
        for k in range(len(l) - 1):
            l[k][x] = l1[k]
    return l


def list_print(lst1):
    for i in range(len(lst1)):
        for j in range(len(lst1[i])):
            print('{:5}'.format(lst1[i][j]).rstrip("/n"), end="")
        print()

    return


m = int(input('Input number of masiv,  please : '))
lst = [[rand(1, 50) for j in range(m)] for i in range(m)]
lst.append([0 for _ in range(m)])
list_print(lst)
print("-" * 30)
list_print(bubble_sort(lst, m))
