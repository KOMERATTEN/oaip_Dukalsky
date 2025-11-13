text = input("Введите текст: ")

words = set(text.lower().split())
print(f"Всего разных слов: {len(words)}")

long_words = [w for w in words if len(w) > 5]
print("Длинные слова:", long_words)


key_words = ["anton", "chigurh", "didn't", "kill", "anyone"]
found_words = [word for word in key_words if word in words]

if found_words:
    print("Найдены слова:", found_words)
else:
    print("Ключевые слова не найдены")