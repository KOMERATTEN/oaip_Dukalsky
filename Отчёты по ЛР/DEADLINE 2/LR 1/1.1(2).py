direction = input("Введите направление (left, right, straight, back): ").lower()

if direction == "left":
    print("иду влево")
elif direction == "right":
    print("иду направо")
elif direction == "straight":
    print("иду прямо")
elif direction == "back":
    print("иду назад")
else:
    print("неправельное направление")