text = input("Введите производный текст: ").lower()
count_dict = {}

for char in text:
    if char in count_dict:
        count_dict[char] += 1
    else:
        count_dict[char] = 1

print(count_dict)