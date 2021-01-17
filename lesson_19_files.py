str = input('Напечатай любой текст: ')

f = open('assets/some1.txt', 'w')
f.write(str)
f.write('End\n')
f.close()

fr = open('assets/some.txt', 'r')
text = fr.read()
fr.close()

print(text)