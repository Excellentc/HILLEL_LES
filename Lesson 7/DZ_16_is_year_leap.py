"""
    Написать функцию is_year_leap, принимающую 1 аргумент — год,
и возвращающую True, если год високосный, и False иначе.
"""


def is_year_leap(n):
    if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
        return True
    else:
        return False


year = int(input('Введите год для проверки : '))
print(year, is_year_leap(year))
