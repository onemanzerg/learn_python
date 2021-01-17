number = 23
running = True
while running:
	guess = int(input('Введите целое число:'))
	if guess == number:
		print('Поздравляю, вы угадали.')
		running = False # Это останавливает цикл while
	elif guess < number:
		print('Нет, загаданное число немного больше этого')
	else:
		print('Нет, загаданное число немного меньше этого')
else:
	print('Цикл while закончен.')
	# Здесь вы можете выполнить всё что вам еще нужно
print('Завершение.')