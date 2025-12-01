import models
import serialize
import random

names = ['Иван', 'Владимир', 'Ярослав', 'Михаил', 'Петр', 'Валерий', 'Дмитрий', 'Аксентий', 'Изяслав']
surnames = ['Иванов', 'Петров', 'Сидоров', 'Обухов', 'Толстой', 'Достоевский', 'Тургенев', 'Пушкин', 'Некрасов']

def gen_full_name():
    name = names[random.randrange(len(names))]
    surname = surnames[random.randrange(len(names))]
    return f'{name} {surname}'

students = [
    models.Student(gen_full_name(), '1990-01-01', f'ГР-{100+random.randrange(100)}', float(random.randrange(5))),
    models.Student(gen_full_name(), '1990-01-01', f'ГР-{100+random.randrange(100)}', float(random.randrange(5))),
    models.Student(gen_full_name(), '1990-01-01', f'ГР-{100+random.randrange(100)}', float(random.randrange(5))),
    models.Student(gen_full_name(), '1990-01-01', f'ГР-{100+random.randrange(100)}', float(random.randrange(5))),
    models.Student(gen_full_name(), '1990-01-01', f'ГР-{100+random.randrange(100)}', float(random.randrange(5))),
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

