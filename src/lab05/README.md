# Лабораторная работа 5
## Задание A — JSON ↔ CSV
Реализовала модуль src/lab05/json_csv.py с функциями, преобразующими json-файл в csv и csv-файл в json.
Вот код к этому заданию:
```
import csv
import json      

def get_json_as_rows(json_path: str):
    """
    Читает содержимое json-файла и возвращает его в виде набора строк.
    """
    with open(json_path, newline="", encoding="utf-8") as f:
        return json.load(f)
    

def get_csv_as_rows(f_name):
    """
    Читает содержимое csv-файла и возвращает его в виде набора строк.
    """
    with open(f_name, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = []
        for row in reader:
            rows.append(row)
        return rows 

    
def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте.
    """
    with open(json_path, encoding="utf-8", newline="") as f:
        try:
            rows = json.load(f)
        except json.decoder.JSONDecodeError:
            raise ValueError("некорректный формат json-файла")
        
    if len(rows) == 0:
        raise ValueError("файл json пустой")
    
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        fieldnames=rows[0].keys()
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()

        for row in rows:
            w.writerow(row)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON. Значения сохраняются как строки.
    """
    rows = []
    
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    if len(rows) == 0:
        raise ValueError("файл-csv пустой")

    with open(json_path, "w", newline='', encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
```
### Вот результат его выполнения:

![скриншот выполения тест-кейсов для задания A](../../images/lab05/img01.png)

## Задание B — CSV -> XLSX

Реализовала модуль src/lab05/csv_xlsx.py, который конвертирует csv-файл в xlsx.
Вот код к этому заданию:

```
from openpyxl import Workbook
from json_csv import *

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX. Колонки — автоширина по длине текста.
    """

    rows = get_csv_as_rows(csv_path)

    if not rows:
        raise ValueError('csv-файл пустой')

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in rows:
        ws.append(row)

    for col in ws.columns:
        max_length = 0
        column = col[0].column_letter # Get the column name
        for cell in col:
            try: # Necessary to avoid error on empty cells
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        if max_length < 8:
            max_length = 8

        adjusted_width = (max_length + 2) * 1.2
        ws.column_dimensions[column].width = adjusted_width

    wb.save(xlsx_path)
```

### Вот результат его выполнения:
![скриншот выполения тест-кейсов для задания B](../../images/lab05/img02.png)

### Вот файл xlsx после обработки:
![xlsx-файл](../../images/lab05/img03.png)