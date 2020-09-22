a = abs(-3)
some = max (4, 7, 2, -1, 0)

# def square(x):
#     return x**2
#
# print(square(25))

# Создайте фунцию, которая будет принимать два числа и символ(+, -, * или /)
# Далее в зависимости от выбранного знака производим операцию с числами и возвращаем через return.
# Если выбран знак / проверяем, чтобы делимое не было меньше делителя!

# def some(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False

def some():
    a = float(input("Введите число A:"))
    b = float(input("Введите число B:"))
    znak = input("Выбирите знак: +,-,*,/\n")
    if znak == "+":
        return a + b
    elif znak == "-":
        return a - b
    elif znak == "*":
        return a * b
    elif znak == "/":
        if a >= b:
            return a / b
        else:
            return "B больше, чем A. Повторите попытку."

print(some())