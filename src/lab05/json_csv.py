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
    if not json_path.endswith('.json'):
        raise ValueError("Неверный тип файла, файл должен иметь расширение json")
    
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
    if not csv_path.endswith('.csv'):
        raise ValueError("Неверный тип файла, файл должен иметь расширение csv")
    
    rows = []
    
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    if len(rows) == 0:
        raise ValueError("файл-csv пустой")

    with open(json_path, "w", newline='', encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)