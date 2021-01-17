#Исключения try, except

a = 100
b = '2'

try:
    c = a / b
except ZeroDivisionError:
    c = 0
    print('Ошибка в делении')
    print('Переменная a =', a)
    print('Переменная b =', b)

