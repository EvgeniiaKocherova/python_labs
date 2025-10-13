def print_arg_ret(func, *a, **kwargs):
    """
    Эта функция пишет аргументы (a) и возвращаемое значение функции (func)
    Используется для отладки тест-кейсов
    """
    print(f'{a} -> ', end='')
    r = func(*a, **kwargs)
    print(r)
    return r

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        s = text.casefold()
    else:
        s = text
    res = []
    words = s.split()
    for word in words:
        new_word = ""
        for i in range(len(word)):
            if yo2e and word[i] == "ё":
                new_word += "е"
            else:
                new_word += word[i]
        res.append(new_word)
    
    return " ".join(res)

assert print_arg_ret(normalize, "ПрИвЕт\nМИр\t") == "привет мир"
assert print_arg_ret(normalize, "ёжик, Ёлка", yo2e=True) == "ежик, елка"
assert print_arg_ret(normalize, "Hello\r\nWorld") == "hello world"
assert print_arg_ret(normalize, "  двойные   пробелы  ") == "двойные пробелы"
assert print_arg_ret(normalize, "ёжик, Ёлка", yo2e=False) == "ёжик, ёлка"
assert print_arg_ret(normalize, "") == ""
assert print_arg_ret(normalize, "   ") == ""
assert print_arg_ret(normalize, "ПрИвЕт\nМИр\t", casefold=False) == "ПрИвЕт МИр"


def is_word_symb(symb):
    return symb.isalpha() or symb.isdigit() or symb == "_"

def tokenize(text: str) -> list[str]:
    res = ""
    for i in range(len(text)):
        s = text[i]
        if is_word_symb(s):
            res += s
        elif s == "-":
            x = " "

            if i > 0 and i < len(text) - 1:
                f = text[i-1]
                a = text[i+1]
                if is_word_symb(f) and is_word_symb(a):
                    x = s
            
            res += x
        else:
            res += " "
    return res.split()

assert print_arg_ret(tokenize, "привет мир") == ["привет", "мир"]
assert print_arg_ret(tokenize, "hello,world!!!") == ["hello", "world"]
assert print_arg_ret(tokenize, "по-настоящему круто") == ["по-настоящему", "круто"]
assert print_arg_ret(tokenize, "2025 год") == ["2025", "год"]
assert print_arg_ret(tokenize, "emoji 😀 не слово") == ["emoji", "не", "слово"]
assert print_arg_ret(tokenize, "") == []
assert print_arg_ret(tokenize, "  двойные   пробелы  ") == ["двойные", "пробелы"]

def count_freq(tokens: list[str]) -> dict[str, int]:
    my_dict = {}
    for i in tokens:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    return my_dict

assert print_arg_ret(count_freq, ["a","b","a","c","b","a"]) == {"a":3,"b":2,"c":1}
assert print_arg_ret(count_freq, ["bb","aa","bb","aa","cc"]) == {"aa":2,"bb":2,"cc":1}
assert print_arg_ret(count_freq, ["bb"]) == {"bb":1}
assert print_arg_ret(count_freq, []) == {}

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    def my_sort(elem):
        return(-elem[1], elem[0])
    
    res = sorted(freq.items(), key=my_sort)
    return res[:n]

assert print_arg_ret(top_n, {"a":3,"b":2,"c":1}, n=2) == [("a",3), ("b",2)]
assert print_arg_ret(top_n, {"aa":2,"bb":2,"cc":1}, n=2) == [("aa",2), ("bb",2)]
assert print_arg_ret(top_n, {"aa":2,"bb":2,"cc":1}, n=0) == []
assert print_arg_ret(top_n, {"aa":2,"bb":2,"cc":1}, n=1) == [("aa",2)]
assert print_arg_ret(top_n, {"aa":2,"bb":2,"cc":1}, n=10) == [("aa",2), ("bb",2), ("cc", 1)]


