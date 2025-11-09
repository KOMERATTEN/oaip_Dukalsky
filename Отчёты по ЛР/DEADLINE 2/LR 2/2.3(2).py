text = input()

letters = 0
digits = 0
punctuation = 0
spaces = 0

for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    elif char in '.,!?:;':
        punctuation += 1
    elif char == ' ':
        spaces += 1

print(f"букв = {letters}")
print(f"цифр = {digits}")
print(f"знаков препинания = {punctuation}")
print(f"пробелов = {spaces}")