import csv
import json
from json_csv import *

print("   ")
print("1 тест-кейс: преобразование people.json в csv")
expected = [
  ["name", "age", "city"],  
  ["Alice", "22", "SPB"],
  ["Bob", "25", "Moscow"],
  ["Carlos", "30", "Kazan"],
  ["Dana", "21", "SPB"],
  ["Andrey", "27", "Novosibirsk"]
]
json_to_csv("../../data/samples/people.json", "../../data/lab05/people_from_json.csv")
csv_rows = get_csv_as_rows("../../data/lab05/people_from_json.csv")
json_rows = get_json_as_rows("../../data/samples/people.json")
print("Ожидаемое содержание csv-файла: ", expected)
print("Фактическое содержание csv-файла: ", csv_rows)
assert csv_rows == expected, (csv_rows, expected)
assert len(csv_rows) - 1 == len(json_rows)  #"-1" потому что первая строка - заголовок

print("   ")
print("###")
print("2 тест-кейс: работа  с пустым json-файлом")
try:
    json_to_csv("../../data/samples/people_empty.json", "./../data/lab05/people_from_json.csv")
    assert False
except ValueError as e:
    print("конвертация пустого json-файла, выкинуто ValueError, как и ожидалось: ", e)

print("   ")
print("###")
print("3 тест-кейс: работа с несуществующим json-файлом")
try:
    json_to_csv("../../data/samples/people_chgh.json", "../../data/lab05/people_from_json.csv")
    assert False
except FileNotFoundError as e:
    print("конвертация несуществующего файла, выкинуто FileNotFoundError, как и ожидалось: ", e)

print("   ")
print("###")
print("4 тест-кейс: работа с json-файлом в кодировке utf-16")
try:
    json_to_csv("../../data/samples/people_utf16.json", "../../data/lab05/people_from_json.csv")
    assert False
except UnicodeDecodeError as e:
    print("конвертация json-файла с неподходящей кодировкой utf-16, выкинуто UnicodeDecodeError, как и ожидалось:", e)

print("   ")
print("###")
print("5 тест-кейс: преобразование people.csv в json")
expected = [
  {"name": "Alice", "age": "22", "city": "SPB"},
  {"name": "Bob", "age": "25", "city": "Moscow"},
  {"name": "Carlos", "age": "30", "city": "Kazan"},
  {"name": "Dana", "age": "21", "city": "SPB"},
  {"name": "Andrey", "age": "27", "city": "Novosibirsk"}
]
csv_to_json("../../data/samples/people.csv", "../../data/lab05/people_from_csv.json")
json_rows = get_json_as_rows("../../data/lab05/people_from_csv.json")
csv_rows = get_csv_as_rows("../../data/samples/people.csv")
print("Ожидаемое содержание json-файла: ", expected)
print("Фактическое содержание json-файла: ", json_rows)
assert json_rows == expected, (json_rows, expected)
assert len(csv_rows) - 1 == len(json_rows)  #"-1" потому что первая строка - заголовок

print("   ")
print("###")
print("6 тест-кейс: работа с пустым csv-файлом")
try:
    csv_to_json("../../data/samples/empty.csv", "../../data/lab05/people_from_json.csv")
    assert False
except ValueError as e:
    print("конвертация пустого csv-файла, выкинуто ValueError, как и ожидалось: ", e)

print("   ")
print("###")
print("7 тест-кейс: работа с несуществующим файлом")
try:
    csv_to_json("../../data/samples/people_chgh.csv", "../../data/lab05/people_from_csv.json")
    assert False
except FileNotFoundError as e:
    print("конвертация несуществующего файла, выкинуто FileNotFoundError, как и ожидалось: ", e)

print("   ")
print("###")
print("8 тест-кейс: работа с csv-файлом в кодировке utf-16")
try:
    csv_to_json("../../data/samples/people_utf16.csv", "../../data/lab05/people_from_csv.json")
    assert False
except UnicodeDecodeError as e:
    print("конвертация csv-файла с неподходящей кодировкой utf-16, выкинуто UnicodeDecodeError, как и ожидалось:", e)

json_to_csv("../../data/samples/people.txt", "../../data/lab05/people_from_json.csv")