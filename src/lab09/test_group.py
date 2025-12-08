from group import Group
from models import Student

def test_group():
    group = Group("test.csv")
    
    s1 = Student("Иван Иванов", "2004-02-22", "БИВТ-25-05", 4.7)
    s2 = Student("Петр Петров", "2004-11-02", "БИВТ-23-03", 3.9)
    s3 = Student("Егор Егоров", "2005-03-15", "БИВТ-25-05", 4.5)
    s4 = Student("Иван Егоров", "2002-03-10", "БИВТ-23-05", 4.5)
    
    print("1. Добавление студентов")
    group.add(s1)
    group.add(s2)
    group.add(s3)
    group.add(s4)
    print(f"   Добавлено: {len(group.list())} студентов")
    
    print("2. Все студенты:")
    for student in group.list():
        print(f"   {student.fio} - {student.group} - {student.gpa}")
    
    print("3. Поиск 'Иван':")
    found = group.find("Иван")
    for student in found:
        print(f"   Найден: {student.fio}")
    
    print("4. Обновление GPA у Ивана:")
    group.update("Иван Иванов", gpa=5.0)
    ivan = group.find("Иван Иванов")[0]
    print(f"   Новый GPA: {ivan.gpa}")
    
    print("5. Удаление Петра")
    group.remove("Петр Петров")
    print(f"   Осталось студентов: {len(group.list())}")
    
    # Тест 6: Финальный вывод
    print("6. Финальный список:")
    for student in group.list():
        print(f"   {student.fio} - {student.gpa}")

test_group()
    