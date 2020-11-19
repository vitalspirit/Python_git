#Задание 1#########################################
def my_func():
    a = input("Введите делимое")
    b = input("Введите делитель")
    try:
        b = int(b)
        a = int(a)
        return a/b
    except ZeroDivisionError:
        print ("Делить на ноль нельзя")
    except (TypeError, ValueError, NameError):
        print ("Введено некорректное значение")
    except:
        print("Неизвестная ошибка")
print(my_func())


#Задание 2#################################################
def user(name, lastname, year_of_birth, city, email, tel):
    print(f"Hello, my name is {name} {lastname}, I was born in {year_of_birth} and I live in {city}. My email is {email} and my telephone number is {tel}.")
user (lastname = "Molchanov", name = "Vitaliy", city = "Taraz", tel = 8888888, email = 'vit@mail.ty', year_of_birth=1985)

#Задание 3################################################
def my_func():
    while True:
        try:
            a = float(input("Enter 1st number"))
            b = float(input("Enter 2nr number"))
            c = float(input("Enter 3rd number"))
        except:
            print ("Wrong input")
            continue
        lst = [a,b,c]
        lst_max = []
        lst_max.append(lst.pop(lst.index(max(lst))))
        lst_max.append(lst.pop(lst.index(max(lst))))
        return sum(lst_max)

print(my_func())

#Задание 4.1####################################################

def my_func():
    while True:
        a = input("Введите действительное положительное число")
        b = input("Введите целое отрицательное число")
        try:
            a = float(a)
            b = int(b)
        except:
            print("Некорректное значение, попробуйте снова")
            continue
        if a > 0 and b < 0:
            return(1/(a**abs(b)))
        else:
            print ("Некорректное значение, попробуйте снова")

print(my_func())

#Задание 4.2###########################################
def my_func():
    while True:
        a = input("Введите действительное положительное число")
        b = input("Введите целое отрицательное число")
        try:
            a = float(a)
            b = int(b)
        except:
            print("Введено неправильное значение. Попробуйте еще раз")
            continue
        result = 1
        if a > 0 and b < 0:
            for n in range(abs(b)):
                result = result*(1/a)
                return (result)
        else:
            print("Некорректное значение, попробуйте снова")
print(my_func())

#Задание 5############################################

def sum_func():
    total_sum = 0
    while True:
        a = input("Введите числа через пробел или 'q' для выхода:  ")
        step_lst_checked = []
        step_sum = 0
        step_lst = a.split()
        for n in step_lst:
            if n != "q":
                step_sum += float(n)
            else:
                total_sum += step_sum
                print(f'{total_sum}')
                return
        total_sum += step_sum
        print(f'{step_sum} ({total_sum})')
sum_func()

#Задание 6##############################
def int_func(str = "nice авп ъghj jапро hjjпаро вапрghgh cool"):
    str_lst = str.split()
    word_list = []
    for n in str_lst:
        latin = False
        for letter in n:
            if ord(letter) in range(65,91) or ord(letter) in range(97,122):
                latin = True
            else:
                latin = False
                break
        if latin == True:
            word_list.append(n.capitalize())
            print(n.capitalize())
        else:
            print("error!")
    return(word_list)
int_func()

#######################################
def int_func_string(str = "this is a lowercase string"):
    print(" ".join(int_func(str)))
int_func_string()
