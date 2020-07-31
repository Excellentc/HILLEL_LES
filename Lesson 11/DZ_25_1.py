
file = open('input.txt', "w", encoding='utf-8')
print("Введите строку для записи в файл. Окончание ввода - ввод пустой строки . ")
while True:
    x = str(input())
    if x == "":
        break
    else:
        file.write(x)
        file.write('\n')
file.close()
