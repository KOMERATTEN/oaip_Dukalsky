temperatures = [15, 18, 12, 20, 16, 14, 19, 17, 13, 21, 15, 16, 18, 20]

max_temp = max(temperatures)
min_temp = min(temperatures)
avg_temp = sum(temperatures) / len(temperatures)

above_avg = 0
for temp in temperatures:
    if temp > avg_temp:
        above_avg += 1

sorted_temps = sorted(temperatures)

fahrenheit = []
for temp in temperatures:
    f = temp * 9/5 + 32
    fahrenheit.append(f)

print(f"Температуры: {temperatures}")
print(f"Максимальная: {max_temp}°C")
print(f"Минимальная: {min_temp}°C")
print(f"Средняя: {avg_temp:.1f}°C")
print(f"Дней выше средней: {above_avg}")
print(f"Отсортированные: {sorted_temps}")
print(f"Фаренгейты: {[round(f, 1) for f in fahrenheit]}")