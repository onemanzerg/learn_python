# Классы и экземпляры

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
        print("Пробег этого авто: " + str(self.odometr) + " км")

    def update_odometr(self, km):
        """Устанавливает пробег"""
        if km >= self.odometr:
            self.odometr = km
        else:
            print("Скрутить одометр не получится")

    def increment_odometr(self, km):
        """Увеличиваем пробег на заданную величину"""
        if km >= 0:
            self.odometr += km
        else:
            print('Не скручивай!')

audi = Car('audi', 'a4', 2017)
subaru = Car('subaru', 'impreza', 2009)

audi.update_odometr(0)
audi.increment_odometr(0)
audi.read_odometr()

subaru.update_odometr(0)
subaru.increment_odometr(14)
subaru.read_odometr()