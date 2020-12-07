#Задание №1 ######################################################################
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def set_date(cls,data):
        day = int(data.split("-")[0])
        month = int(data.split("-")[1])
        year = int(data.split("-")[2])
        return cls(day, month, year)

    @staticmethod
    def validate(n):
        if n.day in range(32) and n.month in range(13) and n.year in range(1985,2024):
            print (True)
        else:
            print(False)

input_date = "31-12-2020"

my_1 = Date.set_date(input_date)
Date.validate(my_1)



#Задание №2 ####################################################################
class DivideByZero(Exception):
   def __init__(self, txt):
      self.txt = txt

def enterage(delimoye, delitel):
   if delitel == 0:
      raise DivideByZero('DIVIZION BY ZERO IS PROHIBITED!!!')
   else:
      print(delimoye/delitel)

try:
   delimoye = int(input('Введите делимое'))
   delitel = int(input('Введите делитель'))
   enterage(delimoye, delitel)
except DivideByZero as err:
    print(err)
except:
   print('Something is wrong')

#Задание №3 ####################################################################
class OnlyNumbers(Exception):
    def __init__(self, txt):
        self.txt = txt
    def __str__(self):
        return self.txt
the_list = []

while True:
    inp_element = input("Введите элемент списка:")
    if inp_element != "stop":
        try:
            if inp_element.isdigit() == True:
                the_list.append(inp_element)
            else:
                raise OnlyNumbers('Error! Only numbers should be entered!!!')
        except OnlyNumbers as err:
            print(err)
    else:
        print(the_list)
        break

# Задание №4 - 5 - 6 ####################################################################
import json


departments = {"1":"HR", "2":"HSE", "3":"Engineering"}
equipment = {"1":"Printer", "2":"Scaner", "3":"Xerox"}


class Departments:
    def __init__(self):
        self.dep_dict = {"HR":{}, "HSE":{}, "Engineering":{}}

class Warehouse:
    def __init__(self, stock):
        self.stock = stock

    def acceptance(self, item_class, new_item):
        if str(item_class).split(".")[1][:-2] not in self.stock.keys():
            self.stock[str(item_class).split(".")[1][:-2]] = []
            self.stock[str(item_class).split(".")[1][:-2]].append(new_item)
        else:
            self.stock[str(item_class).split(".")[1][:-2]].append(new_item)

    def __str__(self):
        return f'В наличии на складе:\n - Принтеры - {len(self.stock["Printer"])} шт.\n - Сканеры' \
               f' - {len(self.stock["Scaner"])} шт.\n' \
               f' - Ксерокс - {len(self.stock["Xerox"])} шт.'
    def transfer_to_department(self):
        while True:
            try:
                self.item_to_transfer = int(input("Что перемещаем? \n1-Принтер \n2-Сканер \n3-Ксерокс"))
                if self.item_to_transfer in [1,2,3]:
                    break
                else:
                    print("Введено неверное значение, попробуйте еще раз")
            except ValueError:
                print("Пожалуйста введите корректное значение (1, 2, 3)")
        while True:
            try:
                self.department = int(input("Куда перемещаем? \n1-HR \n2-HSE \n3-Engineering"))
                if self.department in [1,2,3]:
                    break
                else:
                    print("Введено неверное значение, попробуйте еще раз")
            except ValueError:
                print("Пожалуйста введите корректное значение (1, 2, 3)")
        while True:
            try:
                self.quantity = int(input("введите количество для перемещения:"))
                if self.quantity > len(my_wh.stock[equipment[str(self.item_to_transfer)]]):
                    print("На складе недостаточно запаса")
                else:
                    break
            except ValueError:
                print("Пожалуйста введите корректное значение (число)")

        if equipment[str(self.item_to_transfer)] not in my_dep.dep_dict[departments[str(self.department)]]:
            my_dep.dep_dict[departments[str(self.department)]][equipment[str(self.item_to_transfer)]] = self.quantity
            for i in range(self.quantity):
                my_wh.stock[equipment[str(self.item_to_transfer)]].pop()

class Equipment:
    def __init__(self, manufacturer, model, power_supply,quarantie):
        self.manufacturer = manufacturer
        self.model = model
        self.power_supply = power_supply
        self.quarantie = quarantie

    def transfer_to_warehouse(self):
        my_wh.acceptance(self.__class__, self.__dict__)

class Printer(Equipment):
    def __init__(self, manufacturer, model, power_supply, quarantie, paper_volume, A3_available):
        super().__init__(manufacturer, model, power_supply, quarantie)
        self.paper_volume = paper_volume
        self.A3_available = A3_available

class Scaner(Equipment):
    def __init__(self, manufacturer, model, power_supply, quarantie, max_dpi, A3_available):
        super().__init__(manufacturer, model, power_supply, quarantie)
        self.max_dpi = max_dpi
        self.A3_available = A3_available

class Xerox(Equipment):
    def __init__(self, manufacturer, model, power_supply, quarantie, color, A3_available):
        super().__init__(manufacturer, model, power_supply, quarantie)
        self.color = color
        self.A3_available = A3_available

item1 = Printer("HP", "a320", "220V", "3 years", 400, True)
item2 = Printer("LG", "M540", "220V", "1 years", 300, False)
item3 = Printer("Canon", "XXX", "120V", "2 years", 600, True)
item4 = Scaner("ABB", "FTGF", "220V", "10 years", 2000, False)
item5 = Scaner("Canon", "AD698", "220V", "5 years", 3000, True)
item6 = Xerox("Xerox", "MX-966", "220V", "3 years", True, True)

my_wh = Warehouse({"Printer":[], "Scaner":[], "Xerox":[]})
my_dep = Departments()

def my_func(choice1, choice2, choice3):
    for i in range(choice3):
        if choice1 == 1 and choice2 == 1:
            item1.transfer_to_warehouse()
        elif choice1 == 1 and choice2 == 2:
            item2.transfer_to_warehouse()
        elif choice1 == 1 and choice2 == 3:
            item3.transfer_to_warehouse()
        elif choice1 == 2 and choice2 == 1:
            item4.transfer_to_warehouse()
        elif choice1 == 2 and choice2 == 2:
            item5.transfer_to_warehouse()
        elif choice1 == 3 and choice2 == 1:
            item6.transfer_to_warehouse()



print('Добро пожаловать в прроект "Склад оргтехники"')
while True:
    choice = int(input("Что желаете? \n"
                   "1 - Просмотреть запасы склада\n2 - Переместить новый товар на склад\n3 - Переместить товар со склада\n4 - Детальная информация по складу\n5 - Наличие техники в департаментах"))
    if choice == 1:
        print(my_wh)
    elif choice == 4:
        print(json.dumps(my_wh.stock, indent=2))
    elif choice == 2:
        choice1 = int(input("Какой товар нужно переместить на склад? (1 - принтер, 2 - сканер, 3 - ксерокс)"))
        if choice1 == 1:
            choice2 = int(input("Какой именно принтер перемещаем? (1 - HP, 2 - LG, 3 - Canon)"))
            choice3 = int(input("В каком количестве перемещаем? (число)"))
            my_func(choice1, choice2, choice3)
        if choice1 == 2:
            choice2 = int(input("Какой именно сканер перемещаем? (1 - ABB, 2 - Canon)"))
            choice3 = int(input("В каком количестве перемещаем? (число)"))
            my_func(choice1, choice2, choice3)
        if choice1 == 3:
            choice2 = int(input("Какой именно сканер перемещаем? (1 - xerox)"))
            choice3 = int(input("В каком количестве перемещаем? (число)"))
            my_func(choice1, choice2, choice3)
    elif choice == 3:
        my_wh.transfer_to_department()
    elif choice == 5:
        print (json.dumps(my_dep.dep_dict, indent = 2))


# Задание №7 ####################################################################

class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNumber(4, -8)
z_2 = ComplexNumber(5, 12)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)