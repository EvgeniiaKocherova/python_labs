from openpyxl import Workbook, load_workbook
from json_csv import *
from csv_xlsx import *

print("   ")
print("1 тест-кейс: преобразование cities.csv в xlsx")
csv_to_xlsx("../../data/samples/cities.csv", "../../data/lab05/cities.xlsx")
expected = [
  ("city", "country", "population"),  
  ("SPB", "Russia", "5384342"),
  ("Moscow", "Russia", "13010112"),
  ("Kazan", "Russia", "1306953"),
  ("Novosibirsk", "Russia", "1620162"),
  ("Yekaterinburg", "Russia", "1493749")
]

wb = load_workbook("../../data/lab05/cities.xlsx")
ws = wb["Sheet1"]
xlsx_rows = []
for row in ws.values:
    xlsx_rows.append(row)
csv_rows = get_csv_as_rows("../../data/samples/cities.csv")

print("Ожидаемое содержание xlsx-файла: ", expected)
print("Фактическое содержание xlsx-файла: ", xlsx_rows)

assert expected == xlsx_rows
assert len(csv_rows) == len(xlsx_rows)

print("   ")
print("###")
print("2 тест-кейс: работа с пустым csv-файлом")
try:
    csv_to_xlsx("../../data/samples/empty.csv", "../../data/lab05/empty.xlsx")
    assert False
except ValueError as e:
    print("конвертация пустого csv-файла, выкинуто ValueError, как и ожидалось: ", e)


print("   ")
print("###")
print("3 тест-кейс: работа с несуществующим csv-файлом")
try:
    csv_to_xlsx("../../data/samples/nofile.csv", "../../data/lab05/nofile.xlsx")
    assert False
except FileNotFoundError as e:
    print("конвертация несуществующего csv-файла, выкинуто FileNotFoundError, как и ожидалось: ", e)