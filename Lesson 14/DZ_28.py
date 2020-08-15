"""
    Создать класс, описывающий группу студентов - `Group`. Данный класс хранит студентов в виде списка объектов
`Student` также реализованного в виде соответствующего класса.
    В классах реализовать необходимай набор атрибутов (Например класс `Student` должен иметь атрибуты `name`, `age`,
`grades`), а так же необходимый набор методов экземпляра для работы с этими экземплярами.
"""


class Student:

    def __init__(self, name="", age=0, grade=0):
        self.name = name
        self.age = age
        self.grade = grade


class Group:

    def __init__(self, group=[]):
        self.group = group

    def st_add(self):
        Student.name = str(input("Enter student name : "))
        Student.age = int(input("Enter student age : "))
        Student.grade = int(input("Enter student grade : "))

    def group_st(self):     # Добавление студента
        d = []
        d.append(Student.name)
        d.append(Student.age)
        d.append(Student.grade)
        self.group.append(d)

    def group_pr(self):     # Печать группы
        if len(self.group) == 0:
            print("Group is empty")
        for i in range(len(self.group)):
            for j in range(len(self.group[i])):
                print('{:10}'.format(self.group[i][j]).rstrip("/n"), end="")
            print()

    def st_del(self, name):     #Удаление студента по имени
        for i in range(len(self.group)):
            if name in self.group[i]:
                return self.group.pop(i)


list1 = []
while 1 == 1:
    ch = int(input("Make choice:" "\n"
                   " List group - 1 : ""\n"
                   " Add student - 2 :""\n"
                   " Delete student - 3 : ""\n"
                   " Quit - 4 : "))
    print()
    if ch == 1:     # List group
        x = Group(list1)
        x.group_pr()
        print()
    if ch == 2:     # Add student
        x = Group(list1)
        x.st_add()
        x.group_st()
        print()
    if ch == 3:     # Delete student
        del_student = str(input("Enter name student for delete : "))
        x = Group(list1)
        y = x.st_del(del_student)
        print(del_student, "is delete")
        print()
    if ch == 4:     # Quit
        break
