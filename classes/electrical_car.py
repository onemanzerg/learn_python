from car import  Car

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