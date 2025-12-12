def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a/b 

num1 = float(input("Введите первое число:"))
num2 = float(input("Введите второе число:"))
operation = input("Введите операцию(+, -, *, /):")

if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = add(num1, num2)
elif operation == "*":
    result = add(num1, num2)
elif operation == "/":
    result = add(num1, num2)
else:
    result = "Неизвестная операция"
print("Результат", result)