# Лабораторная работа 2
## Задание 1 — arrays.py
В первом задании я реализую 3 функции: поиск минимума и максимума в списке, сортировка списка по возрастанию и удаление дубликатов, «расплющивание» списка списков/кортежей в один список по строкам.
Вот код к этому заданию.

```
#1
print("задача 1")

def min_max(nums):
    """Эта функция возвращает минимум и максимум из списка.
    Например, [3, -1, 5, 5, 0] -> (-1, 5)"""
    return (min(nums), max(nums))

#2
print("")
print("задача 2")

def unique_sorted(nums):
    """
    Эта функция сортирует значения по возрастанию и убирает дубликаты.
    Например, [3, -1, 5, 5, 0] → (-1, 5)
    """
    return sorted(set(nums))

#3
print("")
print("задача 3")

def flatten0(mat, b):
    """
    Эта функция реализует flatten через рекурсию 
    """
    # print(f'mat={mat}, b={b}')
    for a in mat:
        if type(a) == list:
            flatten0(a, b)
        elif type(a) == tuple:
            flatten0(a, b)
        else:
            if type(a) == str:
                raise TypeError()
            b.append(a)
def flatten(mat):
    """
    Эта функция делает "расплющивание" массива: из вложенного делает плоским
    """
    b = []
    flatten0(mat, b)
    return b
```
![скриншот задания №1](./images/lab02/img01.png)


## Задание 2 - matrix.py
Во втором задании я реализую 3 функции: в матрице меняю строки и столбцы местами, вычисляю сумму по каждой строке, вычисляю сумму по каждому столбцу.
Вот код к этому заданию.

```
#1
print("задача 1")

def transpose(mat):
    """
    Эта функция меняет строки и столбцы местами.
    """
    t_mat = []
    cnt_strok = len(mat) 
    
    if cnt_strok == 0:
        return []
    
    cnt_stl = len(mat[0]) 
    
    for i in range(cnt_stl):
        row = []
        for i in range(cnt_strok):
            row.append(0)

        t_mat.append(row)

    for i in range(cnt_strok):
        for j in range(cnt_stl):
            stroka = mat[i]

            if cnt_stl != len(stroka):
                raise ValueError()
            y = stroka[j]
            t_mat [j][i] = y
    
    return t_mat

#2
print("")
print("задача 2")

def row_sums(mat):
    """
    Эта функция считает сумму в каждой строке матрицы.
    """
    sum_el = []
    cnt_strok = len(mat)
    if cnt_strok == 0:
        return []
    cnt_stl = len(mat[0]) 
    for i in range(cnt_strok):
        sum_el.append(0)
    for i in range(cnt_strok):
        if cnt_stl != len(mat[i]):
            raise ValueError()
        s = 0
        for j in mat[i]:
            s += j
        sum_el[i] = s
    return sum_el

#3
print("")
print("задача 3")

def col_sums(mat):
    """
    Эта функция считает сумму всех столбцов матрицы.
    """
    sum_el = []
    cnt_strok = len(mat)
    
    if cnt_strok == 0:
        return []
    
    cnt_stl = len(mat[0]) 

    for stroka in mat:
        if len(stroka) != cnt_stl:
            raise ValueError()
        
    for i in range(cnt_stl):
        sum_el.append(0)

    for i in range(cnt_strok):
        for j in range(cnt_stl):
            sum_el[j] += mat[i][j]
    
    return sum_el
```
![скриншот задания №2](./images/lab02/img02.png)


## Задание 3 - tuples.py
В третьем задании я работаю с «записями» как с кортежами. Я реализую функцию, которая создает текстовое описания кортежа с данными о студенте.
Вот код к этому заданию.

```
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
```
![скриншот задания №3](./images/lab02/img03.png)



# Лабораторная работа 1
## Задание 1

![скриншот задания №1](./images/lab01/img01.png)


## Задание 2

![скриншот задания №2](./images/lab01/img02.png)


## Задание 3

![скриншот задания №3](./images/lab01/img03.png)


## Задание 4

![скриншот задания №4](./images/lab01/img04.png)


## Задание 5

![скриншот задания №5](./images/lab01/img05.png)