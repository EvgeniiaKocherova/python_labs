import pytest
from pathlib import Path
import sys

sys.path.append("../src/lab08")
from serialize import students_to_json, students_from_json
from models import Student


def test_serialize(tmp_path: Path):
    file = tmp_path / "test.json"
    
    students = [
        Student("Иванов Иван Иванович", "2000-05-15", "SE-01", 4.5),
        Student("Петров Петр Петрович", "2001-08-20", "CS-02", 3.8)
    ]

    students_to_json(students, str(file))
    loaded = students_from_json(str(file))

    assert loaded[0].fio == students[0].fio
    assert loaded[1].fio == students[1].fio

def test_file_no_file():
    with pytest.raises(FileNotFoundError):
        students_from_json("output.json")

def test_wrong():
    with pytest.raises(ValueError):
        students_to_json([], "output.txt")
    
    with pytest.raises(ValueError):
        students_from_json("output.txt")

def test_wrong_json(tmp_path: Path):
    wrong_file = tmp_path / "wrong.json"
    wrong_file.write_text("{wrong json", encoding="utf-8")
    
    with pytest.raises(ValueError):
        students_from_json(str(wrong_file))

def test_not_list(tmp_path: Path):
    with pytest.raises(TypeError):
        students_to_json("не список", str(tmp_path / "test.json"))

    not_list_file = tmp_path / "not_list.json"
    not_list_file.write_text('{}', encoding="utf-8")
    
    with pytest.raises(TypeError):
        students_from_json(str(not_list_file))

def test_not_obj():
    with pytest.raises(TypeError):
        students_to_json([1, 2, 3], "test.json")

