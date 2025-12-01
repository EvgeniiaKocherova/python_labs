import json
from pathlib import Path
from models import *


def students_to_json(students, path):

    json_file = Path(path)

    if not str(json_file).endswith(".json"):
        raise ValueError("неверный тип файла, файл должен иметь расширение json")

    if not isinstance(students, list):
        raise TypeError("students должно быть списком объектов.")

    for s in students:
        if not isinstance(s, Student):
            raise TypeError("все элементы списка должны быть объектами Student.")

    data = []
    for s in students:
        data.append(s.to_dict())

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path):

    json_file = Path(path)

    if not str(json_file).endswith(".json"):
        raise ValueError("неверный тип файла, файл должен иметь расширение json")
    
    if not json_file.exists(): 
        raise FileNotFoundError("файл не найден")

    with open(json_file, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("некорректный формат json-файла")
        except UnicodeDecodeError:
            raise ValueError("Некорректная кодировка файла")

    if not isinstance(data, list):
        raise TypeError("json-файл должен содержать список студентов.")

    students = []
    for item in data:
        if not isinstance(item, dict):
            raise TypeError("каждый студент в json-файле должен быть словарем.")
        students.append(Student.from_dict(item))

    return students