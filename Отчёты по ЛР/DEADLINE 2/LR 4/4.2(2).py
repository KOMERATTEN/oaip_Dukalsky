numbers = list(map(int, input("Введите 10 чисел через пробел: ").split()))

even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

big_numbers = []
for num in numbers:
    if num > 50:
        big_numbers.append(num)

print(f"Исходный список: {numbers}")
print(f"Четные числа: {even_numbers}")
print(f"Числа больше 50: {big_numbers}")