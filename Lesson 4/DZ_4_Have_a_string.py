user_enter = str(input("Введите вашу строку : "))
x = len(user_enter)
print("Третий символ строки : ", user_enter[2])
print("Предпоследний символ строки : ", user_enter[-2])
print("Первые пять символов : ", user_enter[0:5])
print("Вся строки без последних двух символов : ", user_enter[0:x-2:])
print("Все символы с четными индексами : ", user_enter[0::2])
print("Все символы с нечетным индексом : ", user_enter[1::2])
print("Все символы в обратном порядке : ", user_enter[::-1])
print("Все символы через один в обратном порядке : ", user_enter[-x::2])
print("Длина строки : ", x)
