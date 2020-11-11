#Задание 1

a = 5
b = "string"
c = 3.14
d = input("Please enter some integer")
e = a + int(d)
print(e)
f = input("Как Вас Зовут?")
g = input("Сколько Вам лет?")
print(f'Дорогой {f} вам уже {g} лет!')

#Задание 2
timeinseconds = int(input("Enter time in seconds"))
hours = timeinseconds//3600
minutes = (timeinseconds%3600)//60
seconds = (timeinseconds%3600)%60
print(f"{hours}:{minutes}:{seconds}")

#Задание 3
n = input("Please enter n number")
n_sum = int(n) + int(n*2) + int(n*3)
print(n_sum)

#Задание 4 (C "FOR" было бы проще)
num = input("Please enter some positive number")
biggest = 0
x = 0
while x <= len(num)-1:
    if int(num[x]) > biggest:
        biggest = int(num[x])
    x += 1
print(biggest)

#Задание 5
income = int(input("Ваша выручка?"))
expenses = int(input("Ваши издержки?"))
if income > expenses:
    print("Вы работаете в прибыль")
    revenue = income - expenses
    print(f"Ваша прибыль составила{revenue}")
    rent = revenue/income
    print(f"Ваша рентабельность составила{rent}")
    personel = int(input("Сколько у вас сотрудников?"))
    per_person = revenue / personel
    print(f"Прибыль фирмы в расчете на одного сотрудника составила {per_person}")
else:
    print("Вы работаете в убыток")

#Задание 6
a = int(input("Сколько км в первый день?"))
b = int(input("Общее кол-во км?"))

day = 0
km_day = 0
km_total = 0

while km_total <= b:
    if day == 0:
        km_day = a
        km_total = km_total + km_day
        day += 1
    else:
        km_day = km_day*1.1
        km_total = km_total + km_day
        day += 1
print(f"На {day}-й день спортмсмен достиг результата - не менее {b} км")

