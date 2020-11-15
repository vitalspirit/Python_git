#Задание 1
lst = [1, "abc", 3.14, True, {'a':5}, (6,"r",15)]
for a in lst:
    print (f"{a} has a type {type(a)}")

#Задание 2
lst = []
while True:
    i = input("Введите любое число или 'Q' для выхода")
    if i == "Q":
        break;
    else:
        lst.append(i)
print(lst)
for x in range(1,len(lst),2):
    lst[x-1], lst[x] = lst[x], lst[x-1]
print(lst)

#Задание 3.1
month = input("Введите порядковый номер месяца")
зима = [12, 1, 2]
весна = [3, 4, 5]
лето = [6, 7, 8]
осень = [9, 10, 11]

if int(month) in зима:
    print("Зима")
elif int(month) in весна:
    print("Весна")
elif int(month) in лето:
    print("Лето")
elif int(month) in осень:
    print("Осень")
else:
    print('Введено некорректное значение')

#Задание 3.2
month = input("Введите порядковый номер месяца")
year = {"winter":[12, 1, 2], "spring":[3, 4, 5], "лето": [6, 7, 8], "Осень": [9, 10, 11]}
for k,v in year.items():
    if int(month) in v:
        print(k)

#Задание 4
str = input ("Please inter some text")
num = 0
for k in str.split():
    num += 1
    if len(k) > 10:
        print (f'{num}. {k[:10]}')
    else:
        print (f'{num}. {k}')

#Задание 5
my_list = [7, 5, 3, 3, 2]
new = int(input("Enter some number"))

print(my_list.copy())
for x in my_list.copy():
    if my_list.index(x) == len(my_list)-1 and new <= x:
        my_list.append(new)
    elif my_list.index(x) == 0 and new >= x:
        my_list.insert(0, new)
    else:
        if new <= x and new >= my_list[my_list.index(x)+1]:
            print("done")
            my_list.insert(my_list.index(x)+1, new)
            break
print (my_list)
