text = input("Введите текст: ")

# Просто разбиваем по пробелам и убираем знаки препинания
words = []
for word in text.split():
    clean_word = "".join(c for c in word if c.isalpha()).lower()
    if clean_word:
        words.append(clean_word)

if words:
    longest = max(words, key=len)
    shortest = min(words, key=len)
    average = sum(len(w) for w in words) / len(words)
    
    # Считаем слова
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    
    # Сортируем по частоте
    top5 = sorted(counts.items(), key=lambda x: -x[1])[:5]
    
    print("Самое длинное слово:", longest)
    print("Самое короткое слово:", shortest)
    print("Средняя длина:", round(average, 1))
    print("Топ-5 слов:", top5)
else:
    print("Слов не найдено!")