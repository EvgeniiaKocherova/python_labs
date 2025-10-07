def print_arg_ret(func, a):
    """
    Эта функция пишет аргументы (a) и возвращаемое значение функции (func)
    Используется для отладки тест-кейсов
    """
    print(f'{a} -> ', end='')
    r = func(a)
    print(r)
    return r

def get_initials(full_name):
    """
    Эта функция из полного фио делает фамилию + инициалы.
    Например, Иванов Иван Иванович -> Иванов И.И.
    """

    cleaned = ' '.join(full_name.split())
    parts = cleaned.split(' ')
    s = ''
    if len(parts) == 1:
        raise ValueError("неполностью задано фио")
    if len(parts) > 3:
        raise ValueError("Неправильно количество элементов")
    for i in range(len(parts)):
        if i == 0:
            s += parts[i][0].upper() + parts[i][1:] + " "
        else:
            s += parts[i][0].upper() + "."
    return s

def format_record(rec: tuple[str, str, float]) -> str:
    """
    Эта функция создает текстовое описания кортежа с данными о студенте.
    Например, ('Иванов Иван Иванович', 'BIVT-25', 4.6) -> Иванов И.И., гр. BIVT-25, GPA 4.60
    """
    if type(rec) != tuple:
        raise TypeError("неверный тип входных данных")
    fio = rec[0].strip()
    group = rec[1].strip()
    gpa = rec[2]
    if fio == "":
        raise ValueError("fio пустое")
    if group == "":
         raise ValueError("group пустое")
    if type(gpa) != float:
        raise TypeError("неправильный тип данных gpa")
    
    s = f'{get_initials(fio)}, гр. {group}, GPA {gpa:.2f}'

    return s

assert print_arg_ret(format_record, ("Иванов Иван Иванович", "BIVT-25", 4.6)) == "Иванов И.И., гр. BIVT-25, GPA 4.60"
assert print_arg_ret(format_record, ("Петров Пётр", "IKBO-12", 5.0)) == "Петров П., гр. IKBO-12, GPA 5.00"
assert print_arg_ret(format_record, ("Петров Пётр Петрович", "IKBO-12", 5.0)) == "Петров П.П., гр. IKBO-12, GPA 5.00"
assert print_arg_ret(format_record, ("  сидорова  анна   сергеевна ", "ABB-01", 3.999)) == "Сидорова А.С., гр. ABB-01, GPA 4.00"

try:
    print_arg_ret(format_record, ("", "IKBO-12", 5.0))
    assert False, 'не выкинуто исключение, хотя оно ожидалось. Мы не должны сюда дойти'
except ValueError as e:
    print("ValueError: "+ str(e))

try:
    print_arg_ret(format_record, ("  ", "IKBO-12", 5.0))
    assert False, 'не выкинуто исключение, хотя оно ожидалось. Мы не должны сюда дойти'
except ValueError as e:
    print("ValueError: "+ str(e))

try:
    print_arg_ret(format_record, ("Петров Пётр Петрович", "", 5.0))
    assert False, 'не выкинуто исключение, хотя оно ожидалось. Мы не должны сюда дойти'
except ValueError as e:
    print("ValueError: "+ str(e))

try:
    print_arg_ret(format_record, ("Петров Пётр Петрович", "BIVT-25", "b"))
    assert False, 'не выкинуто исключение, хотя оно ожидалось. Мы не должны сюда дойти'
except TypeError as e:
    print("TypeError: " + str(e))

try:
    print_arg_ret(format_record, ("Петров Пётр Петрович", "BIVT-25", 5))
    assert False, 'не выкинуто исключение, хотя оно ожидалось. Мы не должны сюда дойти'
except TypeError as e:
    print("TypeError: " + str(e))

try:
    print_arg_ret(format_record, ("Петров Пётр Петрович", "         ", 5.0))
    assert False, 'не выкинуто исключение, хотя оно ожидалось. Мы не должны сюда дойти'
except ValueError as e:
    print("ValueError: "+ str(e))

try:
    print_arg_ret(format_record, ("Петров", "IKBO-12", 5.0))
    assert False, 'не выкинуто исключение, хотя оно ожидалось. Мы не должны сюда дойти'
except ValueError as e:
    print("ValueError: " + str(e))

try:
    print_arg_ret(format_record, "Петров Пётр Петрович")
    assert False, 'не выкинуто исключение, хотя оно ожидалось. Мы не должны сюда дойти'
except TypeError as e:
    print("TypeError: " + str(e))