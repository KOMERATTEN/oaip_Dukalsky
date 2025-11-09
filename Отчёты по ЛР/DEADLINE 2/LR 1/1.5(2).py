text = input("Введите строку: ")
vowels = "аеёиоуыэюяaeiou"
result = ""
i = 0

while i < len(text):
    if text[i].lower() not in vowels:
        result += text[i]
    i += 1

print(result)