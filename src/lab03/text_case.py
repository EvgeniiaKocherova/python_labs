import sys
sys.path.append("../lib")
from text import *

print("тестирование normalize")
assert print_arg_ret(normalize, "ПрИвЕт\nМИр\t") == "привет мир"
assert print_arg_ret(normalize, "ёжик, Ёлка", yo2e=True) == "ежик, елка"
assert print_arg_ret(normalize, "Hello\r\nWorld") == "hello world"
assert print_arg_ret(normalize, "  двойные   пробелы  ") == "двойные пробелы"
assert print_arg_ret(normalize, "ёжик, Ёлка", yo2e=False) == "ёжик, ёлка"
assert print_arg_ret(normalize, "") == ""
assert print_arg_ret(normalize, "   ") == ""
assert print_arg_ret(normalize, "ПрИвЕт\nМИр\t", casefold=False) == "ПрИвЕт МИр"
print("     ")


print("тестирование tokenize")
assert print_arg_ret(tokenize, "привет мир") == ["привет", "мир"]
assert print_arg_ret(tokenize, "hello,world!!!") == ["hello", "world"]
assert print_arg_ret(tokenize, "по-настоящему круто") == ["по-настоящему", "круто"]
assert print_arg_ret(tokenize, "2025 год") == ["2025", "год"]
assert print_arg_ret(tokenize, "emoji 😀 не слово") == ["emoji", "не", "слово"]
assert print_arg_ret(tokenize, "") == []
assert print_arg_ret(tokenize, "  двойные   пробелы  ") == ["двойные", "пробелы"]
print("     ")

print("тестирование count_freq")
assert print_arg_ret(count_freq, ["a","b","a","c","b","a"]) == {"a":3,"b":2,"c":1}
assert print_arg_ret(count_freq, ["bb","aa","bb","aa","cc"]) == {"aa":2,"bb":2,"cc":1}
assert print_arg_ret(count_freq, ["bb"]) == {"bb":1}
assert print_arg_ret(count_freq, []) == {}
print("     ")


print("тестирование top_n")
assert print_arg_ret(top_n, {"a":3,"b":2,"c":1}, n=2) == [("a",3), ("b",2)]
assert print_arg_ret(top_n, {"aa":2,"bb":2,"cc":1}, n=2) == [("aa",2), ("bb",2)]
assert print_arg_ret(top_n, {"aa":2,"bb":2,"cc":1}, n=0) == []
assert print_arg_ret(top_n, {"aa":2,"bb":2,"cc":1}, n=1) == [("aa",2)]
assert print_arg_ret(top_n, {"aa":2,"bb":2,"cc":1}, n=10) == [("aa",2), ("bb",2), ("cc", 1)]


