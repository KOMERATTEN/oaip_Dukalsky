path = input("Введите направление (left, right, straight, back): ")
if path == "left":
    print("Иду влево")
elif path == "right":
    print("Иду вправо")
elif path == "straight":
    print("Иду прямо")
elif path == "back":
    print("Иду назад")
else:
    print("Неправильное направление")