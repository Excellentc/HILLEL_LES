num = int(input("Введите 3x значное число для изменения : "))
print("Ваш перевертыш будет = ", num % 10 * 100 + num // 10 % 10 * 10 + num // 100)
