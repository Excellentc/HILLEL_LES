"""
    Реализовать класс цифрового счетчика. Обеспечьте возможность установки максимального и минимального значений,
увеличения счетчика на 1, возвращения текущего значения.

"""


class Count:

    def __init__(self, go=None, stop=None):
        self.go = go
        self.stop = stop

    def up(self):
        if self.go < self.stop:
            self.go += 1
            return self.go
        else:
            return 'Its over'


e = int(input("Введите начало отсчета : "))
w = int(input("Введите конец отсчета : "))
count_1 = Count(go=e, stop=w)
for _ in range(e, w + 1):
    print(count_1.up())
