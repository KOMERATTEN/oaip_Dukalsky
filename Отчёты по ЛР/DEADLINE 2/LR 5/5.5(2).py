math_students = {"Валодя", "Сашка", "Никитка", "Максимка"}
physics_students = {"Сашка", "Никитка", "Максимка", "Артёмка"}
cs_students = {"Валодя", "Максимка", "Никитка", "Сашка"}

all_three = set()
for student in math_students:
    if student in physics_students and student in cs_students:
        all_three.add(student)


only_one = set()
all_students = set()
for student in math_students: all_students.add(student)
for student in physics_students: all_students.add(student)
for student in cs_students: all_students.add(student)


for student in all_students:
    count = 0
    if student in math_students: count += 1
    if student in physics_students: count += 1
    if student in cs_students: count += 1
    if count == 1:
        only_one.add(student)


math_only = set()
for student in math_students:
    if student not in physics_students:
        math_only.add(student)

print(f"Все три курса: {all_three}")
print(f"Только один курс: {only_one}")
print(f"Математика: {math_only}")
print(f"Всего студентов: {len(all_students)}")
