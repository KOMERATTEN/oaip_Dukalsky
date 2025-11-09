symbol = input("Символ: ")
height = int(input("Высота: "))
width = int(input("Ширина: "))

i = 0
while i < height:
    j = 0
    while j < width:
        print(symbol, end="")
        j += 1
    print()
    i += 1