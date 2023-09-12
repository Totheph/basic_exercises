# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика


students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
names = []
for dictt in students:
    names.append(dictt["first_name"])
print(names)
for name in names:
    print(f"{name}: {names.count(name)}")
    names.remove(name)

# Задание 2

#Через люмбду, мне кажется, тут удобнее всего:
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
names = [dictt["first_name"] for dictt in students]
print("Самое частое имя среди учеников:", max(names, key= lambda x: names.count(x)))

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.


school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

for students in school_students:
    names = [dictt["first_name"] for dictt in students]
    print(f"Самое частое имя в классе {school_students.index(students)+1}:", max(names, key= lambda x: names.count(x)))

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]}
]

is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

def gender_count(name_list):
    girls_count = 0
    boys_count = 0
    for name in name_list:
        if is_male[name]:
            boys_count += 1
        else:
            girls_count += 1
    return [girls_count, boys_count]

for school_class in school:
    names = [pair["first_name"] for pair in school_class["students"]]
    girls, boys = gender_count(names)
    print(f"Класс {school_class['class']}: девочки {girls}, мальчики {boys}")



# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков



#Мне кажется, что я тут намудрила....

#И простите за люмбды)

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

def gender_count(name_list):
    girls_count = 0
    boys_count = 0
    for name in name_list:
        if is_male[name]:
            boys_count += 1
        else:
            girls_count += 1
    return [girls_count, boys_count]


for school_class in school:
    names = [pair["first_name"] for pair in school_class["students"]]
    school_class["genders"] = gender_count(names)


print("Больше всего мальчиков в классе", max(school, key=lambda sch_class: sch_class["genders"][1])["class"])
print("Больше всего девочек в классе", max(school, key=lambda sch_class: sch_class["genders"][0])["class"])