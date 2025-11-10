# Лабораторная работа 6
## 1

Реализовала модуль src/lab06/cli_text.py с подкомандами:

stats --input <txt> [--top 5] — анализ частот слов в тексте;  
cat --input <path> [-n] — вывод содержимого файла построчно.

Вот код к этому заданию:
```
import argparse
import sys
sys.path.append("../lib")
from text import * 

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    sub = parser.add_subparsers(dest="cmd")

    cat_parser = sub.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Имя входного файла со словами")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = sub.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="Имя входного файла со словами")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество самых частых слов, которые нужно вывести")

    args = parser.parse_args()

    try:
        if args.cmd == "stats":
            with open(args.input, 'r', encoding='utf-8') as f:
                text = f.read()
            norm_text = normalize(text)
            tokenz = tokenize(norm_text)
            freqs = count_freq(tokenz)
            top_n1 = top_n(freqs, n=args.top)
            
            for i in top_n1:
                print(f"{i[0]}:{i[1]}")
        elif args.cmd == "cat":
            with open(args.input, 'r', encoding='utf-8') as f:
                cnt = 1
                for line in f:
                    s = line.rstrip()

                    if args.n:
                        s = f'{cnt}: {s}'
                        cnt += 1

                    print(s)
    except FileNotFoundError:
        print(f"файл \"{args.input}\" не найден")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
### Вот результат работы команды cat:

![скриншот выполения cat](../../images/lab06/img01.png)

### Вот результат работы команды stats:

![скриншот выполения stats](../../images/lab06/img02.png)

## 2

Реализовала модуль src/lab06/cli_convert.py с подкомандами:

json2csv --in data/samples/people.json --out data/out/people.csv - преобразование json файла в csv  
csv2json --in data/samples/people.csv --out data/out/people.json - преобразование csv файла в json   
csv2xlsx --in data/samples/people.csv --out data/out/people.xlsx - преобразование csv файла в xlsx    

Вот код к этому заданию:

```
import argparse
import sys
sys.path.append("../lab05")
from json_csv import json_to_csv, csv_to_json
from csv_xlsx import csv_to_xlsx

def main():

    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv", help="Конвертировать из json в csv")
    p1.add_argument("--in", dest="input", required=True, help="Входной json файл")
    p1.add_argument("--out", dest="output", required=True, help="Итоговый csv файл")

    p2 = sub.add_parser("csv2json", help="Конвертировать из csv в json")
    p2.add_argument("--in", dest="input", required=True, help="Входной csv файл")
    p2.add_argument("--out", dest="output", required=True, help="Итоговый json файл")

    p3 = sub.add_parser("csv2xlsx", help="Конвертировать из csv в xlsx")
    p3.add_argument("--in", dest="input", required=True, help="Входной csv файл")
    p3.add_argument("--out", dest="output", required=True, help="Итоговый xlsx файл")

    args = parser.parse_args()

    try:
        if args.cmd == "json2csv":
            json_to_csv(args.input, args.output)
        elif args.cmd == "csv2json":
            csv_to_json(args.input, args.output)
        else:
            csv_to_xlsx(args.input, args.output)
    except FileNotFoundError:
        print(f"файл \"{args.input}\" не найден")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

### Вот выполнения всех подкоманд:
![скриншот выполения всех подкоманд](../../images/lab06/img03.png)

![скриншот выполения всех подкоманд](../../images/lab06/img04.png)
