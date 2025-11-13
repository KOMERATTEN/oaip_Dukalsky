students = [
    ("Валодя", 18, 4.0),
    ("Максимка", 18, 4.5),
    ("Никитка", 33, 4.9),
    ("Сашка", 6, 4.7),
    ("Артёмка", 99, 4.3)
]

print("Старше 20 лет:")
for name, age, aver_score in students:
    if age > 20:
        print(f"{name}, {age}, балл: {aver_score}")

best_aver_score = 0
best_name = ""
for name, age, aver_score in students:
    if aver_score > best_aver_score:
        best_aver_score = aver_score
        best_name = name
print(f"Лутший студен: {best_name}, балл: {best_aver_score}")

print("Студенты по алфавиту:")
for name, age, aver_score in sorted(students):
    print(f"{name}, {age}, балл: {aver_score}")

 