user_input = str(input("Введиет Вашу строку : "))
x1 = int(user_input.find("h")+1)
x2 = int(user_input.rfind("h"))
y = user_input[x1:x2:]
print(user_input[:x1:]+y.replace("h", "H", len(y)+1)+user_input[x2::])
