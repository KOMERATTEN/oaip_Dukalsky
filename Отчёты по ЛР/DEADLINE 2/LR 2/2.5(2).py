n = int(input("Сколько чисел вы хотите ввести? "))

numbers = []
for i in range(n):
    num = int(input(f"Введите число {i + 1}: "))
    numbers.append(num)

maximum = max(numbers)
minimum = min(numbers)
average = sum(numbers) / n

count_above_avg = 0
for num in numbers:
    if num > average:
        count_above_avg += 1

print("\nРезультаты:")
print(f"Максимальное: {maximum}")
print(f"Минимальное: {minimum}")
print(f"Среднее: {average}")
print(f"Чисел больше среднего: {count_above_avg}")