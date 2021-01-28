#import  car # import all module car.py

from car import *   # import all module car.py
from  electrical_car import ElectricCar

a4 = Car('audi', 'a4', 2010)
print(a4.description_name())

tesla = ElectricCar('tesla', 's', 2018)
tesla.battery.description_battery()
tesla.description_battery()