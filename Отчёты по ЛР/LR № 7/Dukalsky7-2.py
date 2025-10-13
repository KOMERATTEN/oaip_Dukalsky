passw = input("Придумайте пароль: ")
confir = input("Подтвердите пароль: ")
if passw != confir:
    print("Пароли не совпадают!")
else:
    print("Пароль успешно установлен!")
    login = input("Введите пароль для входа: ")
    if login == passw:
        print("Access")
    else:
        print("Denied")