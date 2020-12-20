# Запись в файл
# str = input('Напечатай любой текст: ')
# f = open('some.txt', 'a')
# f.write(str)
# f.close()

# Чтение файла
fr = open('some.txt', 'rt')
# text = fr.read(12)
# fr.close()
# print(text)

for line in fr:
    print(line)
fr.close()