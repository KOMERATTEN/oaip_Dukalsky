text = ""
while True:
    line = input()
    if line == "":
        break
    text += line + " "

words = text.lower().split()
stats = {}

for word in words:
    word = word.strip('.,!?;:')
    if word in stats:
        stats[word] += 1
    else:
        stats[word] = 1

print(f"Статистика слов: {stats}")