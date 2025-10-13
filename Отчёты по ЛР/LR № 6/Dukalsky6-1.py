surname, name, patronymic = input("Введите ФИО: ").split()
fio = f"{surname.title()} {name.title()} {patronymic.title()}"
print(f"Добро пожаловать {fio}")