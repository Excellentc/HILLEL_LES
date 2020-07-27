from string import ascii_uppercase, digits


def convert_to(num, to_num=10):
    num_new = ''
    x = digits + ascii_uppercase
    if 2 > to_num or to_num > 32:
        return "Неправильный ввод системы исчисления"
    else:
        while num > 0:
            num_new = x[num % to_num] + num_new
            num //= to_num
    return num_new


x1 = int(input("Введите конечную систему исчисления : "))
n1 = int(input("Введите число для перевода в др. систему исчисления  от 2 до 32 : "))
print(convert_to(n1, x1))
