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


while 1 == 1:
    e = int(input("Введите начало отсчета : "))
    w = int(input("Введите конец отсчета : "))
    if e > w or e == w:
        print("Начала отсчета должно быть меньше, чем конец отсчета, введите параметры заного.")
    else:
        break
count_1 = Count(go=e, stop=w)
for _ in range(e, w + 1):
    print(count_1.up())
