some = 111 # global variable

def var1():
    some = 222 # local variable
    print(some)

def var2():
    print(some)

# def gender(sex='Unknown'):
#     if sex == 'm':
#         sex = 'Male'
#     elif sex == 'f':
#         sex == 'Female'
#     else:
#         sex = 'Unknown'
#     return sex
#
# print(gender())

ziga = 0

def first_func(): # прибавляет 5 к глобальной переменной и печатает результат
    guk = ziga + 5
    print(guk)

def second_func(): # меняет глобальную переменную с 0 на 10
    global ziga
    ziga = ziga + 10
    return ziga

first_func()
second_func()

print(ziga)


# Создайте глобальную переменную со значением 0
# Создайте две функции
# Первая добавляет 5 к текущей переменной и печатает это в принт
# Вторая добавляет 10 к глобальной переменной и возвращает ее же через return
# Распечатайте после вызова обеих функций глобальную переменную и посмотрите на ее значение