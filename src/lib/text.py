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
    """
    Эта функция "очищает" текст: приводит к нижнему регистру, заменяет ё на е, убирает лишние управляющие символы и пробелы.
    """
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

def is_word_symb(symb):
    """
    Эта функция проверяет, является ли символ допустимым для слова.
    """
    return symb.isalpha() or symb.isdigit() or symb == "_"

def tokenize(text: str) -> list[str]:
    """
    Эта функция разбивает входной текст на список слов по небуквенно-цифровым разделителям.
    """
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


def count_freq(tokens: list[str]) -> dict[str, int]:
    """
    Эта функция подсчитывает частоту появления каждого слова в списке.
    """
    my_dict = {}
    for i in tokens:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    return my_dict

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """
    Эта функция возвращает список из n самых частых слов.
    """
    def my_sort(elem):
        return(-elem[1], elem[0])
    
    res = sorted(freq.items(), key=my_sort)
    return res[:n]
