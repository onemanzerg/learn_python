# Списки

lists = [213, 123, 'asda', 12.2]

# Множества

names = {'Ivan', 'Oleg', 'Masha', 'Sasha', 'Ivan', 'sasha'}
# print(len(names))

# Словари (ключ:значение)

class_room = {'Ivan':'27', 'Sasha':'30', 'Masha':'18'}

# print(class_room['Sasha'])

# for k, v in class_room.items():
#     print(k)

# питонтьютор пример

# Создадим пустой словать Capitals
Capitals = dict()

# Заполним его несколькими значениями
Capitals['Russia'] = 'Moscow'
Capitals['Ukraine'] = 'Kiev'
Capitals['USA'] = 'Washington'

Countries = ['Russia', 'France', 'USA', 'Russia']

for country in Countries:
    # Для каждой страны из списка проверим, есть ли она в словаре Capitals
    if country in Capitals:
        print('Столица страны ' + country + ': ' + Capitals[country])
    else:
        print('В базе нет страны c названием ' + country)

