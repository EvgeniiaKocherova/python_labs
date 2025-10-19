import sys
sys.path.append("../lib")
from text import *
from io_txt_csv import read_text, write_csv
# f_name = "../../data/lab04/input.txt"
# f_name = "../../data/lab04/empty_file.txt"
f_name = "../../data/lab04/test-cp1251.txt"
# input_encoding = "utf-8"
input_encoding = "cp1251"
# output_encoding = "utf-8"
output_encoding = "cp1251"
try:
    text = read_text(f_name, encoding=input_encoding)
except FileNotFoundError:
    print(f"Файла {f_name} не существует")
    sys.exit(1)


norm_text = normalize(text)
tokenz = tokenize(norm_text)
freqs = count_freq(tokenz)
top_5 = top_n(freqs, n=5)

rows = freqs.items()

def my_sort(elem):
    return(-elem[1], elem[0])

rows = sorted(rows, key=my_sort)
write_csv(rows, "../../data/lab04/report.csv", encoding = output_encoding, header=("word", "count"))

print(f"Всего слов: {len(tokenz)}")
print(f"Уникальных слов: {len(freqs.keys())}")
print(f"Топ-5:")
for i in top_5:
    print(f"{i[0]}:{i[1]}")





