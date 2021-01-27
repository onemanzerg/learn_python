# Классы и экземпляры, наследование

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

class Battery():
    """Just accumulator model for ElectricCar"""

    def __init__(self, battery=100):
        self.battery = battery

    def description_battery(self):
        """Выводит инфо об уровне баттареи"""
        print("Этот автомобиль имеет аккумулятор мощностью " + str(self.battery) + " MAph")

class ElectricCar(Car):
    """Аспекты для электромобиля"""
    def __init__(self, make, model, year):
        """Инициализация атрибутов класса родителя"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def description_battery(self):
        """Выводит инфо об уровне баттареи"""
        print("%s %s %s" % (self.make, self.model, self.year) + " имеет аккумулятор мощностью: " + str(self.battery) + " MAph")

    def description_name(self):
        """Переопределение родительского метода"""
        desc = str(self.year) + ' ' + self.make + ' ' + self.model
        return desc.title()


if __name__ == "__main__":
    tesla = ElectricCar('tesla', 's', 2018)
    tesla.battery.description_battery()
    tesla.description_battery()

    audi = Car('audi', 'a4', 2017)
    subaru = Car('subaru', 'impreza', 2009)

    audi.update_odometr(0)
    audi.increment_odometr(0)
    audi.read_odometr()

    subaru.update_odometr(5)
    subaru.increment_odometr(12)
    subaru.read_odometr()