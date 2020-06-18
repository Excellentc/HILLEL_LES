while 1 == 1:
    user_input = str(input("Введиет Вашу строку : "))
    if user_input.count("h") > 1:
        break
    else:
        print("Повторите ввод пожалуйста")
x1 = int(user_input.find("h")+1)
x2 = int(user_input.rfind("h"))
y = user_input[x1:x2:]
print("\t\t\t\t\t  "+user_input[:x1:]+y.replace("h", "H", len(y)+1)+user_input[x2::])
