sibvol = input("Символ: ")
visota = int(input("Высота: "))
shirina = int(input("Ширина: "))

i = 0
while i < visota:
    j = 0
    while j < shirina:
        if i == 0 or i == visota - 1 or j == 0 or j == shirina - 1:
            print(sibvol, end="")
        else:
            print(" ", end="")
        j += 1
    print()
    i += 1