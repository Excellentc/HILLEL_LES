
def cl_form(lst_h):
    s_sr, cx = 0, 0
    for j in range(2, len(lst_h)):
        s_sr += float(lst_h[j])
        cx += 1
    if s_sr/cx < 5:
        print('{:<20}'.format(lst_h[1] + " " + lst_h[0]), '{:>20}'.format(round(s_sr / cx, 2)))
    return lst_h[1] + " " + lst_h[0][0]+".", round(s_sr/cx, 2)


lst, lst1 = [], []
c = 0
file_class = open('class_list.py', encoding='utf-8')
for lin in file_class:
    lst.append(lin.strip('\n').split())
file_class.close()

print(" Студенты, с средним баллом меньше 5-ти")
print()
for i in range(len(lst)):
    lst1.append(cl_form(lst[i]))
    c += lst1[i][1]

file = open('stud_list.txt', "w", encoding='utf-8')
file.write('{:<33}'.format("Фамилия И."))
file.write('{:<20}'.format("Ср. балл:"))
file.write('\n')
for i in range(len(lst1)):
    file.write('{:<20}'.format(lst1[i][0]))
    file.write('{:>20}'.format(lst1[i][1]))
    file.write('\n')
file.close()

print('{:<20}'.format("Средний балл по классу :"), '{:>16}'.format(round(c/len(lst1), 2)))
print()
