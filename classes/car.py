class Car():
    """Класс по созданию автомобиля"""
    def __init__(self, make, model, year):
        """Инициализация атрибутов автомобиля"""
        self.make = make
        self.model = model
        self.year = year
        self.odometr = 0

    def description_name(self):
        """Возвращаем описание автомобиля"""
        desc = str(self.year) + ' ' + self.make + ' ' + self.model
        return desc.title()

    def read_odometr(self):
        """Выводим пробег авто"""
        print("Пробег %s %s %s" % (self.make, self.model, self.year) + " года выпуска: " + str(self.odometr) + " км")

    def update_odometr(self, km):
        """Устанавливает пробег"""
        if km >= self.odometr:
            self.odometr = km
        else:
            print("Это автомобиль, а не машина времени")

    def increment_odometr(self, km):
        """Увеличиваем пробег на заданную величину"""
        if km >= self.odometr:
            self.odometr += km
        else:
            print('Не скручивай!')