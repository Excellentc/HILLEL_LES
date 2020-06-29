
summ = 0
for i in range(3):
    klas_piple = int(input(f"Введите количество учеников в классе {i+1} : "))
    summ = summ + (klas_piple + klas_piple % 2)/2
print("Общее количество парт", summ)
