###           Задание №1                                  #####
import time
class TrafficLight:
    def running(self):
        self.__color = "red"
        print(self.__color)
        time.sleep(7)
        self.__color = "yellow"
        print(self.__color)
        time.sleep(2)
        self.__color = "green"
        print(self.__color)
        time.sleep(5)
a=TrafficLight()
a.running()

###           Задание №2                                  #####
class Road:
    _length = float(input("What is the road length in meters?"))
    _width = float(input("What is the road width in meters?"))
    _thickness = float(input("What is the road thickness in cantimeters?"))
    def mass_calc(self):
        return self._length*self._width*25*self._thickness

my_road = Road()
print(f"Масса асфальта необходимого для данных параметров составляет {my_road.mass_calc()/1000} тонн")

###           Задание №3                                  #####
dict_1 = {"wage": 15000, "bonus": 5000}

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)
    def get_full_name(self):
        return self.name + " " + self.surname
    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

a = Position("Max", "Ivanov", "engineer", dict_1)
print(a.get_full_name())
print(a.get_total_income())

###           Задание №4                                  #####
import random as rd
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f"{self.color} {self.name} started moving")
    def stop(self):
        print(f"{self.color} {self.name} has stopped movement")
    def turn(self):
        if rd.randint(1,10) > 5:
            print(f"{self.color} {self.name} has turned left")
        else:
            print(f"{self.color} {self.name} has turned right")
    def show_speed(self):
        print(f"{self.color} {self.name}'s speed is {self.speed} km/h")

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"ATTENTION!!! Car speed is {self.speed} km/h which is higher then the allowed 60 km/h")
        else:
            print(f"Car speed is {self.speed} km/h")
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"ATTENTION!!! Car speed is {self.speed} km/h which is higher then the allowed 40 km/h")
        else:
            print(f"Car speed is {self.speed} km/h")
class PoliceCar(Car):
    pass

t = TownCar(85, "Black", "Volvo", False)
t.show_speed()
w = WorkCar(39, "Red", "Toyota", False)
w.show_speed()
p = PoliceCar(100, "Blue", "Lada", True)
p.turn()
s = SportCar(240, "Orange", "Ferrari", False)
s.go()

###           Задание №4                                  #####
class Stationary:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f"Запуск отрисовки")

class Pen(Stationary):
    def draw(self):
        print(f"Запуск отрисовки с помощью ручки {self.title} ")

class Pencil(Stationary):
    def draw(self):
        print(f"Запуск отрисовки с помощью карандаша {self.title} ")

class Handle(Stationary):
    def draw(self):
        print(f"Запуск отрисовки с помощью маркера {self.title} ")

type_1 = Pen("Maped")
type_2 = Pencil("Стрела")
type_3 = Handle("Cool")
type_1.draw()
type_2.draw()
type_3.draw()