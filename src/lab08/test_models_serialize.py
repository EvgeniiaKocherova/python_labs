import models
import serialize
import random

names = ['Иван', 'Владимир', 'Иван', 'Михаил', 'Петр', 'Иван', 'Дмитрий', 'Петр', 'Егор']
surnames = ['Иванов', 'Петров', 'Сидоров', 'Иванов', 'Иванов', 'Михайлов', 'Егоров', 'Петров', 'Сидоров']

def gen_full_name():
    name = names[random.randrange(len(names))]
    surname = surnames[random.randrange(len(names))]
    return f'{name} {surname}'

students = [
    models.Student('Петр Иванов', '1990-01-01', 'SE-01', 4.0),
    models.Student('Иван Егоров', '1990-01-01', 'SE-110', 3.5),
    models.Student('Иван Иванов', '1990-01-01', 'SE-11', 5.0),
    models.Student('Петр Петров', '1990-01-01', 'SE-02', 2.5),
    models.Student('Иван Егоров', '1990-01-01', 'SE-20', 3.0),
]

print('*** 1) ДЕМО ПЕЧАТИ СТУДЕНТОВ ***')

for i, student in enumerate(students):
    print(f'{i+1} {student}')

print('*** 2) ДЕМО СЕРИАЛЗАЦИИ СТУДЕНТОВ ***')
serialize.students_to_json(students, 'students.json')

print('*** 3) ДЕМО ДЕСЕРИАЛЗАЦИИ СТУДЕНТОВ ***')
students = serialize.students_from_json('students.json')

for i, student in enumerate(students):
    print(f'{i+1} {student}')
