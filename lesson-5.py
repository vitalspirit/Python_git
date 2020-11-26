# Задание 1 #############################################################
with open("file1.txt", "w") as my_file:
    while True:
        inp = input("Please enter some text")
        if inp.isspace() or inp == "":
            break
        else:
            print(inp, file = my_file)

# Задание 2 #############################################################
with open("task2.txt", "r") as my_file:
    string_count = 0
    word_count = {}
    for i in my_file.readlines():
        string_count += 1
        word_count[string_count] = len(i.split())
    print(f"Total number of strings in the file is {string_count}")
    for k,v in word_count.items():
        print(f"Line #{k} has {v} words")

# Задание 3 ###############################################
with open("text_3.txt", "r", encoding = "utf-8") as my_file:
    print("Сотрудники с заработной платой менее 20000р.:")
    total_salary = 0
    staff = 0
    for i in my_file.readlines():
        staff += 1
        total_salary += float(i.split()[1])
        if float(i.split()[1]) < 20000:
            print(f" - {i.split()[0]}")
        else:
            continue
    print(f"Средняя величина дохода сотрудников: {total_salary/staff}р.")

# Задание 4 ###############################################

from googletrans import Translator
translator = Translator()
with open("text_4.txt", "r", encoding = "utf-8") as my_file:
    with open("text_4_1.txt", "w") as my_file_1:
        for line in my_file.readlines():
            print(translator.translate(line.split()[0], src='en', dest='ru').text + " " + line.split()[1] + " " + line.split()[2], file=my_file_1)

# Задание 5 ###############################################
def myfunc(str):
    with open("task5.txt", "a+", encoding="utf-8") as my_file:
        sum = 0
        for i in str.split():
            my_file.write(i + " ")
        my_file.seek(0)
        for v in my_file.read().split():
            sum += float(v)
        print(sum)

myfunc("1 22 33     100")

# Задание 6 ###############################################
with open("text_6.txt", "r", encoding="utf-8") as my_file:
    dict = {}
    for line in my_file.readlines():
        lessons = 0
        for word in line.split():
            if "(" in word:
                lessons += int(word[:word.index("(")])
        dict[line.split(":")[0]] = lessons
    print(dict)

# Задание 7 ###############################################
import json
with open("text_7.txt", "r", encoding="utf-8") as my_file:
    dict1 = {}
    dict2 = {}
    total_profit = 0
    profitable = 0
    for line in my_file.readlines():
        profit = int(line.split()[-2]) - int(line.split()[-1])
        dict1[line.split()[0]] = profit
        if profit > 0:
            total_profit += profit
            profitable += 1
    dict2["average_profit"] = total_profit/profitable
    result = [dict1, dict2]
    print(result)
    with open("text7_1.json", "w",  encoding="utf-8",) as my_json:
        json.dump(result, my_json, ensure_ascii=False, indent = 2)
