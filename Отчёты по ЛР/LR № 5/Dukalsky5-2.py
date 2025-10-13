x, y, z = map(int, input("\nВведите 3 целых числа через пробел: ").split())
mul1, mul2, mul3 = x*y, y*z, z*x
pow4, mod, div = x**4, y%z, z//x
print(f"\nУмножение: {mul1}, {mul2}, {mul3}")
print(f"Степень/остаток/деление: {pow4}, {mod}, {div}")
print(f"Сумма результатов: {pow4 + mod + div}")