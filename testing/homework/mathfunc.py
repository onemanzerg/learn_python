"""Напишите математическую функцию со знаками “+”, “-”, “*” и “/”, которая умеет принимать три параметра
1-е число, 2-е число и один из четырех математических знаков.
Два первых параметра обязательны, если третий параметр (знак) не введен ставим по умолчанию знак “+”
Распишите тесты для этой функции
"""

def math_func (first, second, znak):
    """Отдает полное имя и фамилию пользователя"""
    if znak == '+':
        answer = first + second
    elif znak == '':
        answer = first + second
    elif znak == '-':
        answer = first - second
    elif znak == '*':
        answer = first * second
    elif znak == '/':
        answer = first / second
    else:
        print("Вы ввели неверный знак. Попробуйте снова")