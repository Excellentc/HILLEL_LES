import random


def pr_tabl(l2):
    for c in l2:
        for x in c:
            if x == 0:
                print("{:6c}".format(x), end="")
            else:
                print("{:6d}".format(x), end="")
        print()


n = int(input("Введите количество строк : "))
m = int(input("Введите количество колонок : "))
lst2 = [[random.randint(1, 100) for j in range(m)] for i in range(n)]

for i in range(n):    # Считаем, заполняем сумму по рядам"
    sum_line = 0
    for j in range(m):
        sum_line += lst2[i][j]
    lst2[i].append(0)
    lst2[i].append(sum_line)

lst_help = []
for i in range(m):      # Считаем, заполняем сумму по столбцам"
    sum_line = 0
    for j in range(n):
        sum_line += lst2[j][i]
    lst_help.append(sum_line)
lst2.append([0 for i in range(n)])
lst2.append(lst_help)

pr_tabl(lst2)
