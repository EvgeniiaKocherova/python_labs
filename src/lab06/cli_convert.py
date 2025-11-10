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