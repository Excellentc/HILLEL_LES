x1 = int(input("Введите координату расположения \"Коня\", по оси Х : "))  # Ввод координат старых
y1 = int(input("Введите координату расположения \"Коня\", по оси Y : "))
while 1 == 1:
    x2 = int(input("Введите координаты следующего хода \"Коня\", по оси Х : "))  # Ввод координат новых
    y2 = int(input("Введите координаты cледующего хода \"Коня\", по оси У : "))
    if (x1 - x2 == 1 and y2 - y1 == 2) or (x2 - x1 == 1 and y2 - y1 == 2) or \
            (x2 - x1 == 2 and y2 - y1 == 1) or (x2 - x1 == 2 and y1 - y2 == 1) or \
            (x2 - x1 == 1 and y1 - y2 == 2) or (x1 - x2 == 1 and y1 - y2 == 2) or \
            (x1 - x2 == 2 and y1 - y2 == 1) or (x1 - x2 == 2 and y2 - y1 == 1):
        print("Да, за один ход конь попадет на новую клетку.")
        print("-" * 60)
    else:
        print("К сожалению, конь не доберется за один ход на эту клетку")
        print("-" * 60)
    quii = input("Хотите проверить новые координаты? Y/N : ")
    if quii == "N" or quii == "n":
        break
