"""
    Вам на вход приходит последовательность целых чисел. Вам надо обрабатывать ее следующим образом: выводить на экран
сумму первых пяти чисел этой последовательности, затем следующих 5 итд.
    Но последовательность не дается вам сразу целиком. С течением времени к вам поступают её последовательные части.
Например, сначала первые три элемента, потом следующие шесть, потом следующие два и т. д.
    Реализуйте класс Buffer, который будет накапливать в себе элементы последовательности и выводить сумму пятерок
последовательных элементов по мере их накопления.
    Одним из требований к классу является то, что он не должен хранить в себе больше элементов, чем ему действительно
 необходимо, т. е. он не должен хранить элементы, которые уже вошли в пятерку, для которой была выведена сумма.
"""


class Buffer:
    def __init__(self):  # конструктор без аргументов
        self.list_numbers = []

    def student_add(self, a):  # добавить следующую часть последовательности\
        self.list_numbers += a
        for i in range(0, len(self.list_numbers), 5):
            if len(self.list_numbers) < 5:
                return print("Numbers out. You need add new ", 5 - len(self.list_numbers), " numbers")
            print("Summa = ", sum(self.list_numbers[0:5:1]), " for numbers : ", self.list_numbers[0:5])
            self.list_numbers = self.list_numbers[5::]

    # Честно говоря не понимаю для чего этот метод может использоваться
    # def get_current_part(self):
    # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены


print(" Enter a sequence of natural numbers. ", "\n",
      "For END INPUT- enter empty line : ", '\n',
      "For QUIT - enter Q", "\n")
l1 = []
amp = Buffer()
while 1 == 1:
    x = input("Input you sequence numbers  :   ")
    if x == "q" or x == "Q":
        print("You are QUIT")
        break
    elif x == "":
        amp.student_add(l1)
        l1 = []
    else:
        l1.append(int(x))
