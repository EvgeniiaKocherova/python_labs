import pytest
import csv
import json
from pathlib import Path
import sys

sys.path.append("../src/lab05")
from json_csv import *


# 1
def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


# 2
def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    data = """name,age,city
Alice,22,SPB
Bob,25,Moscow
Carlos,30,Kazan
Dana,21,SPB
Andrey,27,Novosibirsk
"""
    expected = [
        {"name": "Alice", "age": "22", "city": "SPB"},
        {"name": "Bob", "age": "25", "city": "Moscow"},
        {"name": "Carlos", "age": "30", "city": "Kazan"},
        {"name": "Dana", "age": "21", "city": "SPB"},
        {"name": "Andrey", "age": "27", "city": "Novosibirsk"},
    ]
    src.write_text(data, encoding="utf-8")
    csv_to_json(str(src), str(dst))

    json_rows = get_json_as_rows(str(dst))
    csv_rows = get_csv_as_rows(str(src))
    assert json_rows == expected, (json_rows, expected)
    assert len(csv_rows) - 1 == len(json_rows)


# 3
def test_json_to_csv_city(tmp_path: Path):
    src = tmp_path / "cities.json"
    dst = tmp_path / "cities.csv"
    data = [
        {"name": "Alice", "age": 22, "city": "SPB"},
        {"name": "Bob", "age": 25, "city": "Moscow"},
        {"name": "Carlos", "age": 30, "city": "Kazan"},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 3
    assert {"name", "age", "city"} <= set(rows[0].keys())


# 4
def test_json_to_csv_empty(tmp_path: Path):
    src = tmp_path / "empty.json"
    dst = tmp_path / "empty.csv"
    src.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


# 5
def test_csv_to_json_no_file():
    with pytest.raises(FileNotFoundError):
        csv_to_json("nofile.csv", "output.json")


# 6
def test_json_to_csv_no_file():
    with pytest.raises(FileNotFoundError):
        json_to_csv("nofile.json", "output.csv")


# 7
def test_json_to_csv_wrong(tmp_path: Path):
    src = tmp_path / "wrong.json"
    dst = tmp_path / "wrong.csv"
    src.write_text("hello world", encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


# 8
def test_csv_to_json_wrong(tmp_path: Path):
    src = tmp_path / "wrong.csv"
    dst = tmp_path / "wrong.json"
    src.write_text("hello world", encoding="utf-8")

    with pytest.raises(ValueError):
        csv_to_json(str(src), str(dst))
