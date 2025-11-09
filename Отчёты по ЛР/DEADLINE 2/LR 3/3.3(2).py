phone_book = {}

while True:
    print("\n1 - Показать все контакты")
    print("2 - Добавить контакт")
    print("3 - Удалить контакт")
    print("4 - Выйти")
    
    choice = input("Выберите действие: ")
    
    if choice == "1":
        for name, phone in phone_book.items():
            print(f"{name}: {phone}")
    
    elif choice == "2":
        name = input("Введите имя: ")
        if name in phone_book:
            print("Контакт с таким именем уже существует")
        else:
            phone = input("Введите телефон: ")
            phone_book[name] = phone
            print("Контакт добавлен")
    
    elif choice == "3":
        name = input("Введите имя для удаления: ")
        if name in phone_book:
            del phone_book[name]
            print("Контакт удален")
        else:
            print("Контакт не найден")
    
    elif choice == "4":
        exit()
    
    else:
        print("Неверный выбор")