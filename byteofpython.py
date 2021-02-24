'''
number = 23
running = True
while running:
    guess = int(input('Введите целое число : '))
    if guess == number:
        print('Поздравляю, вы угадали.')
        running = False # это останавливает цикл while
    elif guess < number:
        print('Нет, загаданное число немного больше этого.')
    else:
        print('Нет, загаданное число немного меньше этого.')
else:
    print('Цикл while закончен.')
# Здесь можете выполнить всё что вам ещё нужно
print('Завершение.')


while True:
    s = input('Введите что-нибудь : ')
    if s == 'выход':
        break
    print('Длина строки:', len(s))
print('Завершение')
'''


# while True:
#     s = input('Введите что-нибудь : ')
#     if s == 'выход':
#         break
#     if len(s) < 3:
#         print('Слишком мало')
#         continue
#     print('Введённая строка достаточной длины')
# Разные другие действия здесь...

# Функции (нелокальная переменная)

# def func_outer():
#     x = 2
#     print('x равно', x)
#
#     def func_inner():
#         nonlocal x
#         x = 8
#     func_inner()
#     print('Локальное x сменилось на', x)
#
# func_outer()

def total(a=5, *numbers, **phonebook):
    print('a:', a)

    # проход по всем элементам кортежа
    for single_item in numbers:
        print('single_item', single_item)

    # проход по всем элементам словаря
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


print(total(10, 1, 2, 3, 4, Jack=1123, John=2231, Inge=1560, Alex=1488))
