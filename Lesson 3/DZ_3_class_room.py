sum = 0
for i in range(3):
    while 1 == 1:
        klas_pip = int(input(f"Введите количество учеников в классе {i+1} : "))
        if klas_pip >= 0:
            break
        else:
            print("Количество учеников не должно быть отрицательным\n")
    if klas_pip == 0:
        sum = sum
    elif klas_pip % 2 == 0:
        sum = sum + klas_pip / 2
    else:
        sum = sum + klas_pip // 2 +1
print("Общее количество парт", sum)
