text = input("Введите текст: ")
old, new = input("Введите строку1 строку2: ").split()
print(f"Результат: {text.replace(old, new)}")