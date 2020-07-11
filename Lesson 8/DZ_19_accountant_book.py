
"""
Напишите программу на Python, которая на вход получает список списков
и возвращает список кортежей. Каждый кортеж состоит из номера заказа и произведения
цены на товары и количества. Стоимость товара должена быть увеличена на $10, если
стоимость заказа меньше $100. Программа должна использовать lambda и map.
"""

lst = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]
# С использованием map lambda
en = list(map(lambda x: (x[0], x[2] * x[3]) if x[2]*x[3] > 100 else (x[0], round(x[2] * (x[3]+10), 2)), lst))
print(en)

#  Без map и lambda
# for i in range(len(lst)):
#     if lst[i][2]*lst[i][3] < 100:
#         lst[i] = (lst[i][0], round(lst[i][2]*(lst[i][3]+10), 2))
#     else:
#         lst[i] = (lst[i][0], round(lst[i][2] * lst[i][3], 2))
# print(lst)
