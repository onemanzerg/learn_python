"""Создайте основной класс ресторан
создайте атрибуты еды, напитков (до 5 штук)
Добавьте методы посадочных  мест, время работы, количество сотрудников
Создайте дочерний класс уголок кальяна
добавьте атрибуты сорты табака
добавьте метод заказать кальян

Если вы выполняли домашнее задание с прошлого занятия о пользователях сайта, тогда:
создайте класс администратор, который наследуется от базового пользователя
добавьте атрибут привилегии
Добавьте метод вывода перечня привилегий администратора

Доработка сегодняшнего занятия
Добавьте в класс Батарей метод разряда батареи, который принимает параметр пробега и внутри умножает
пробега на расход батареии и потом отнимает данные с атрибута батареи
Добавьте метод заряда батарей к 100% значению"""

class Restaurant():
    """Main class restaurant"""
    def __init__(self, name, food, drink, alco, lunch, water):
        """Initialize atts of restaurant"""
        self.name = name
        self.food = food
        self.drink = drink
        self.alco = alco
        self.lunch = lunch
        self.water = water
        self.free = 50

    def guest(self, free):
        """Vivodit kolichestvo svobodnih mest"""
        if free <= self.free:
            self.free -= free
            print("Осталось %s" % (self.free) + " мест")
        else:
            print("Нет мест")

    def work_time(self):
        """Output work time"""
        print("Ресторан %s" % (self.name) + " работает с 10-00 до 22-00")

class SmokeLounge(Restaurant):
    """Aspects for a lounge zone"""
    def __init__(self, musthave, alfaker, easy):
        self.musthave = musthave
        self.alfaker = alfaker
        self.easy = easy
        """Initialize parents atts"""

    def hookah(self, hook):
        if hook == self.musthave:
            print("Вы заказали кальян с табаком Мастхэв")



kfc = Restaurant('kfc', 'cheeseburger', 'cola', 'beer', 'bites', 'aqua')
kfc.work_time()
kfc.guest(0)

hookahhouse = SmokeLounge()
hookahhouse.hookah('alfaker')
