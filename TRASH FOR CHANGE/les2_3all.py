def tabl(): # рисуем рамку
    print(1)
a = 0   #счетчик попыток ввода
while a < 3:
    choise = input("Какие escape-последовательности вывести на экран ?\n"
                "\t\t\t\\n - New line     -- [1]\n"
                "\t\t\t\\a - Bell (alert) -- [2]\n"
                "Введите число от 1 до 6 через пробел: ").split()
    a+=1
    for i in range (choise):
        
