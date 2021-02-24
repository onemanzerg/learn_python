from testing import full_name

print("Для остановки теста введите символ 'Q'")

while True:
    first = input("Введите ваше имя: ")
    if first == 'Q':
        break
    last = input("Введите вашу фамилию: ")
    if last == 'Q':
        break

    format_name = full_name(first, last)
    print("Форматирование имени: " + format_name)