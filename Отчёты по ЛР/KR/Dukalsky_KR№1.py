tel = input("Введите номер телефона: ")
if (len(tel) == 16 and 
    tel[0:3] == "+7-" or tel[6:10:13] == "-" and 
    (tel[3:6] + tel[7:10] + tel[11:13] + tel[14:16]).isdigit() and
    tel[3] == "9"):
    print("Соединяем")
else:
    print("Неправельно набран номер")
