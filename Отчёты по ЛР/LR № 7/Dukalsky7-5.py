import math
data = input("Введите число, знак и число: ").split()
num1 = float(data[0])
znak = data[1]
num2 = float(data[2])
if znak == '+':
    print(num1 + num2)
elif znak == '-':
    print(num1 - num2)
elif znak == '*':
    print(num1 * num2)
elif znak == '/':
    print(num1 / num2)
elif znak == '%':
    print(num1 % num2)
elif znak == '//':
    print(num1 // num2)
elif znak == '**':
    print(num1 ** num2)
elif znak == '%%':
    print((num2 / 100) * num1)
elif znak == '/**':
    print(math.sqrt(num1))
else:
    print("Неизвестная операция")