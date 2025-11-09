text = input("Введите строку: ")

text = text.lower().replace(" ", "")

left = 0
right = len(text) - 1

while left < right:
    if text[left] != text[right]:
        print("Это не палиндром")
        break
    left += 1
    right -= 1
else:
    print("Это палиндром!")