import pytest
import sys
import os

sys.path.append("../src/lab08")
from models import * 

class TestStudentValidation:
    """Тесты для валидации данных студента"""

    # Тесты для ФИО
    def test_fio_not_str(self):
        with pytest.raises(TypeError):
            Student(fio=123, birthdate="2000-01-01", group="SE-01", gpa=4.5)

    def test_fio_empty(self):
        with pytest.raises(TypeError):
            Student(fio="", birthdate="2000-01-01", group="SE-01", gpa=4.5)

    def test_fio_is_spaces(self):
        with pytest.raises(TypeError):
            Student(fio="   ", birthdate="2000-01-01", group="SE-01", gpa=4.5)

    def test_fio_wrong(self):
        with pytest.raises(TypeError):
            Student(fio="Иванов Иван123", birthdate="2000-01-01", group="SE-01", gpa=4.5)

    def test_fio_one_word(self):
        with pytest.raises(TypeError):
            Student(fio="Иванов", birthdate="2000-01-01", group="SE-01", gpa=4.5)

    def test_fio_small(self):
        with pytest.raises(TypeError):
            Student(fio="иванов иван", birthdate="2000-01-01", group="SE-01", gpa=4.5)

    def test_fio_dash(self):
        student = Student(fio="Петров-Иванов Иван Иванович", birthdate="2000-05-15", group="SE-01", gpa=4.5)
        assert student.fio == "Петров-Иванов Иван Иванович"

    # Тесты для даты рождения
    def test_birthdate_not_str(self):
        with pytest.raises(ValueError):
            Student(fio="Иванов Иван", birthdate=20000101, group="SE-01", gpa=4.5)

    def test_birthdate_wrong_length(self):
        with pytest.raises(ValueError):
            Student(fio="Иванов Иван", birthdate="2000-01-1", group="SE-01", gpa=4.5)

    def test_birthdate_wrong_format(self):
        with pytest.raises(ValueError):
            Student(fio="Иванов Иван", birthdate="2000/01/01", group="SE-01", gpa=4.5)

    def test_birthdate_letter(self):
        with pytest.raises(TypeError):
            Student(fio="Иванов Иван", birthdate="2000-ab-01", group="SE-01", gpa=4.5)

    def test_birthdate_wrong(self):
        with pytest.raises(ValueError):
            Student(fio="Иванов Иван", birthdate="2000-13-01", group="SE-01", gpa=4.5)

#    def test_birthdate_future_date(self): ???


    # Тесты для GPA
    def test_gpa_not_float(self):
        with pytest.raises(ValueError):
            Student(fio="Иванов Иван", birthdate="2000-01-01", group="SE-01", gpa="4.5")

    def test_gpa_less_zero(self):
        with pytest.raises(ValueError):
            Student(fio="Иванов Иван", birthdate="2000-01-01", group="SE-01", gpa=-1.0)

    def test_gpa_more_five(self):
        with pytest.raises(ValueError):
            Student(fio="Иванов Иван", birthdate="2000-01-01", group="SE-01", gpa=5.1)

    def test_gpa_max_min(self):
        Student(fio="Иванов Иван", birthdate="2000-01-01", group="SE-01", gpa=0.0)
        Student(fio="Петров Петр", birthdate="2000-05-15", group="SE-01", gpa=5.0)

    # Тесты для группы
    def test_group_not_str(self):
        with pytest.raises(TypeError):
            Student(fio="Иванов Иван", birthdate="2000-01-01", group=101, gpa=4.5)

    def test_group_empty(self):
        with pytest.raises(ValueError):
            Student(fio="Иванов Иван", birthdate="2000-01-01", group="", gpa=4.5)

    def test_group_is_spaces(self):
        with pytest.raises(ValueError):
            Student(fio="Иванов Иван", birthdate="2000-01-01", group="   ", gpa=4.5)

    def test_group_short(self):
        with pytest.raises(ValueError):
            Student(fio="Иванов Иван", birthdate="2000-01-01", group="SE", gpa=4.5)