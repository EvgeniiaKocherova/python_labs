import csv
import os
from io_txt_csv import read_text, write_csv



print("проверка, что возвращается одна строка")
txt2 = read_text("../../data/lab04/input2.txt")
assert type(txt2) == str

print("проверка, что если файл не найден — поднимается FileNotFoundError")
try:
    read_text("../../data/lab04/input3.txt")
    assert False
except FileNotFoundError:
    print("read_txt вызван для несуществующего файла, поймано исключение FileNotFoundError, как и ожидалось ")

print("проверка, что если кодировка не та, поднимается UnicodeDecodeError")
try:
    read_text("../../data/lab04/test-cp1251.txt", encoding = "utf-8")
    assert False
except UnicodeDecodeError:
    print("указана кодировка utf-8, а файл записан в кодировке cp1251, поймано исключение UnicodeDecodeError, как и ожидалось")

print("проверка, что при обработке пустого файла выведется пустая строка")
txt_em = read_text("../../data/lab04/empty_file.txt")
assert txt_em == ""

print("проверка, что csv-файл создается с разделителем запятая")
write_csv([("word","count"),("test",3)], "../../data/lab04/check01.csv")
with open("../../data/lab04/check01.csv") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        assert len(row) == 2

print("проверка, что если передан header, то он запишется первой строкой")
write_csv([("word","count"),("test",3)], "../../data/lab04/check02.csv", header=("h1", "h2"))
with open("../../data/lab04/check02.csv") as f:
    r = csv.reader(f)
    for row in r:
        assert row == ["h1",  "h2"], row
        break

print("проверка, что все строки имеют одинаковую длину, а если нет, то поднимается ValueError")
try:
    write_csv([("word","count"),("test",3, "elem1")], "../../data/lab04/check03.csv")
    assert False
except ValueError:
    print("write_csv вызвано со строчками разной длины, перехвачено ValueError, как и ожидалось")

print("проверка, что если rows пустой, то формируется пустой csv файл")
write_csv([], "../../data/lab04/check04.csv")
txt3 = read_text("../../data/lab04/check04.csv")
assert txt3 == ""

print("проверка, что если файл с header=(a,b), то файл содержит только заголовок")
write_csv([], "../../data/lab04/check05.csv", header=("a", "b"))
with open("../../data/lab04/check05.csv") as f:
    r = csv.reader(f)
    for row in r:
        assert row == ["a", "b"] 
