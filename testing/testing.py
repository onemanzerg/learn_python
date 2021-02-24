# Тестирование в Python

def full_name(first, last, second=''):
    """Отдает полное имя и фамилию пользователя"""
    if second:
        full = first + ' ' + last + ' ' + second
    else:
        full = first + ' ' + last
    return full.title()