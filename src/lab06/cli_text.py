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