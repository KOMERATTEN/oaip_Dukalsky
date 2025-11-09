grades = []

grades.append(5)
grades.append(4)
grades.append(3)
grades.append(5)
grades.append(2)

print(f"Текущие оценки: {grades}")

grades.pop(0)
grades.pop()

average = sum(grades) / len(grades)

print(f"Средний балл: {average}")
print(f"Итоговые оценки: {grades}")
