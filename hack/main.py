import random

def generate_good_password(lenght=10):
    # Задать алфавит
    alphabet = 'abcdefghiklmnoprstquvwxyz'\
                'ABCDEFGHIKLMNOPRSTQUVWXYZ'\
                '1234567890!@#$%^&*()[]{}<>,.'

    # return ''.join(random.choices(alphabet, k=lenght))

    # Выбрать случайный символ из алфавита
    # Повторить 2 пункт lenght раз
    # Склеить символы в строку

    password = ''
    for i in range(lenght):
        # symbol = random.choice(alphabet)
        password += random.choice(alphabet)

    return password

#print(generate_good_password(5))
#print(generate_good_password())

popular_passwords_data


popular_passwords = [
    '123456',
    '12345',
    'admin',
    'qwerty',
    ''
]

i = 0

def generate_bad_password():
    global i

    if i >= len(popular_passwords):
        return

    password = popular_passwords[i]
    i += 1
    return password

print(generate_bad_password())
print(generate_bad_password())
print(generate_bad_password())
