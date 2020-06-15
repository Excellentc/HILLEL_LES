summ = 0
for i in range(3):
    while 1 == 1:
        klas_pip = int(input(f"Введите количество учеников в классе {i+1} : "))
        if klas_pip >= 0:
            break
        else:
            print("Количество учеников не должно быть отрицательным\n")
    if klas_pip == 0:
        summ = summ
    elif klas_pip % 2 == 0:
        summ = summ + klas_pip / 2
    else:
        summ = summ + klas_pip // 2 +1
print("Общее количество парт", summ)
