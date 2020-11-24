# Задание 1 #############################################################
from sys import argv

script_name, working_hours, hour_rate, extra_sallary = argv
monthly = (float(working_hours)*float(hour_rate))+float(extra_sallary)

print("Имя скрипта: ", script_name)
print("Кол-во часов: ", working_hours)
print("Ставка в час: ", hour_rate)
print("Премия: ", extra_sallary)
print("Месячная заработная плата составила: ", monthly)

# Задание 2 #############################################################
lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_lst = [a for a in lst if lst.index(a)>0 and a > lst[lst.index(a)-1]]
print(new_lst)

# Задание 3 #############################################################
lst = [a for a in range(20,241) if a%20 == 0 or a%21 == 0]
print(lst)

# Задание 4 #############################################################
lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_lst = [a for a in lst if lst.count(a) == 1]
print(new_lst)

# Задание 5 #############################################################
from functools import reduce

lst = [v for v in range(100,1001) if v % 2 == 0]
result = reduce((lambda a,b: a*b), lst)
print(result)

# Задание 6 #############################################################
from itertools import count
from itertools import cycle
def my_func(count_start = 100, count_step = 5, lst = ["apple", "orange", "banana"]):
    for i in count(count_start,count_step):
        if i > 200:
            total = 0
            for v in cycle(["apple", "orange", "banana"]):
                if total > 50:
                    return ("Count() and Cycle() functions both used successfully")
                else:
                    total += 1
                    print(f"Cycle() function used --> {v}")
        else:
            print(f"Count() function used --> {i}")
print(my_func())
# Задание 7 #############################################################

def fact(n):
    value = 1
    for i in range(1,n+1):
        value *=i
        yield value
factorial = fact(10)
for i in factorial:
    print(i)
