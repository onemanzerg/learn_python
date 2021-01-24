"""Ресторан: создайте класс с именем Restaurant Метод __init__() класс Restaurant должен содержать два атрибута:
restaurant_name и cuisine_type

Создайте метод describe_
restaurant(), который выводит два атрибута, и метод open_restaurant(), который выводит
сообщение о том, что ресторан открыт

Создайте на основе своего класса экземпляр с именем restaurant Выведите два атрибута по отдельности,
затем вызовите оба метода

Три ресторана:
Создайте три разных экземпляра, вызовите для каждого экземпляра метод describe_restaurant()

Пользователи:
создайте класс с именем User Создайте два атрибута first_name и last_
name, а затем еще несколько атрибутов, которые обычно хранятся в профиле пользователя

Напишите метод describe_user(), который выводит сводку с информацией о пользователе

Создайте еще один метод greet_user() для вывода персонального приветствия для
пользователя

Создайте несколько экземпляров, представляющих разных пользователей
Вызовите оба метода для каждого пользователя"""

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        """Ресторан: создайте класс с именем Restaurant Метод __init__() класс Restaurant
        должен содержать два атрибута: restaurant_name и cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Создайте метод describe_restaurant(), который выводит два атрибута"""
        print(self.cuisine_type.title() + ' ' + self.restaurant_name.title())

    def close_restaurant(self):
            """Создайте метод describe_restaurant(), который выводит два атрибута"""
            print(self.cuisine_type.title() + ' ' + self.restaurant_name.title() + ": Мы закрыты!")

    def open_restaurant(self):
        """Содайте метод open_restaurant(), который выводит
        сообщение о том, что ресторан открыт"""
        print(self.cuisine_type.title() + ' ' + self.restaurant_name.title() + ": Мы открылись!")

KFC = Restaurant('KFC', 'Fastfood')

KFC.open_restaurant()
KFC.close_restaurant()
