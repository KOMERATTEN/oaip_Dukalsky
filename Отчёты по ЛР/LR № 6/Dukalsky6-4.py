text = input("Введите текст: ")
start, end = map(int, input("Введите диапазон (например: 2 5): ").split())
print(f"Подстрока: {text[start-1:end]}")