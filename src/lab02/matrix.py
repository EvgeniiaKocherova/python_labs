def g(func, a):
    print(f'{a} -> ', end='')
    r = func(a)
    print(r)
    return r

#1
print("задача 1")

def transpose(mat):
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

assert g(transpose, [[1, 2, 3]]) == [[1], [2], [3]]
assert g(transpose, [[1], [2], [3]]) == [[1, 2, 3]]
assert g(transpose, [[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
assert g(transpose, []) == []
try:
    g(transpose, [[1, 2], [3]])
    assert False
except ValueError:
    print("ValueError")

try:
    g(transpose, [[1], [2, 3]])
    assert False
except ValueError:
    print("ValueError")

#2
print("")
print("задача 2")

def row_sums(mat):
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

assert g(row_sums, [[1, 2, 3], [4, 5, 6]]) == [6, 15]
assert g(row_sums, [[-1, 1], [10, -10]]) == [0, 0]
assert g(row_sums, [[0, 0], [0, 0]]) == [0, 0]
try:
    g(row_sums, [[1, 2], [3]])
    assert False
except ValueError:
    print("ValueError")
assert g(row_sums, []) == [] 

#3
print("")
print("задача 3")

def col_sums(mat):
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

assert g(col_sums, [[1, 2, 3], [4, 5, 6]]) == [5, 7, 9]
assert g(col_sums, [[-1, 1], [10, -10]]) == [9, -9]
assert g(col_sums, [[0, 0], [0, 0]]) == [0, 0]
try:
    g(col_sums, [[1, 2], [3]])
    assert False
except ValueError:
    print("ValueError")
assert g(col_sums, []) == []


