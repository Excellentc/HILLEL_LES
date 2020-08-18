"""
    Создать класс, описывающий группу студентов - `Group`. Данный класс хранит студентов в виде списка объектов
`Student` также реализованного в виде соответствующего класса.
    В классах реализовать необходимай набор атрибутов (Например класс `Student` должен иметь атрибуты `name`, `age`,
`grades`), а так же необходимый набор методов экземпляра для работы с этими экземплярами.
"""


class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


class Group:
    def __init__(self, student_list):
        self.st_list = student_list

    def student_add(self, x, y, c):
        self.st_list.append((x, y, c))

    def group_print(self):     # Print group
        if len(self.st_list) == 0:
            print("Group is empty")
        for i in range(len(self.st_list)):
            for j in range(len(self.st_list[i])):
                print('{:10}'.format(self.st_list[i][j]).rstrip("/n"), end="")
            print()

    def student_del(self, name):     # Delete student by name
        for i in range(len(self.st_list)):
            if name in self.st_list[i]:
                return self.st_list.pop(i)


l1 = []
while 1 == 1:
    ch = int(input("Make choice:" "\n"
                   " List group - 1 : ""\n"
                   " Add student - 2 :""\n"
                   " Delete student - 3 : ""\n"
                   " Quit - 4 : "))
    print()
    if ch == 1:     # List group
        x = Group(l1)
        x.group_print()
        print()

    if ch == 2:     # Add student
        n1 = str(input("Enter student name : "))
        a1 = int(input("Enter student age : "))
        g1 = int(input("Enter student grade : "))
        stu = Student(n1, a1, g1)
        group_st = Group(l1)
        group_st.student_add(stu.name, stu.age, stu.grade)
        print()

    if ch == 3:     # Delete student
        del_student = str(input("Enter name student for delete : "))
        x = Group(l1)
        y = x.student_del(del_student)
        print(del_student, "is delete")
        print()
    if ch == 4:     # Quit
        print("You are quit")
        break
