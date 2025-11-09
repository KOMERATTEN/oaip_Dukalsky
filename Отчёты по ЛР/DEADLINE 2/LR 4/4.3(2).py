tasks = []

while True:
    print("\n1 - Показать все задачи")
    print("2 - Добавить задачу")
    print("3 - Отметить задачу как выполненную")
    print("4 - Выйти")
    
    choice = input("Выберите действие: ")
    
    if choice == "1":
        if tasks:
            print("Ваши задачи:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("Задач нет")
    
    elif choice == "2":
        task = input("Введите задачу: ")
        tasks.append(task)
        print(f"Задача '{task}' добавлена")
    
    elif choice == "3":
        if tasks:
            print("Ваши задачи:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            num = int(input("Какую задачу выполнили? "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num-1)
                print(f"Задача '{removed}' удалена!")
            else:
                print("Неверный номер")
        else:
            print("Задач нет")
    
    elif choice == "4":
        break

print("До свидания!")