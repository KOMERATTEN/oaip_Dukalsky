def simple_calculator(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b

result = simple_calculator(10, 5, '*')
print(result)