# Класс

class Dog():
    """Простая модель собаки"""

    def __init__(self, name, age):
        """Инициализируем атрибуты имя и вораст"""
        self.name = name
        self.age = age

    def sit(self):
        """Собака будет садиться по команде"""
        print(self.name.title() + ": Собака села!")

    def jump(self):
        """Собака будет садиться по команде"""
        print(self.name.title() + ": Собака подпрыгнула!")

    def gav(self):
        """Собака будет садиться по команде"""
        print(self.name.title() + ": Гав-гав!")

my_dog = Dog('Topik', 4)
my_dog_2 = Dog('Nick', 7)
Poppy = Dog('Poppy', 2)

#print(my_dog.age)
#print(my_dog.name)

my_dog.jump()
my_dog_2.sit()
Poppy.gav()