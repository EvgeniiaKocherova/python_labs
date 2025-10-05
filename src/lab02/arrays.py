def g(func, a):
    print(f'{a} -> ', end='')
    r = func(a)
    print(r)
    return r
    
#1
print("задача 1")

def min_max(nums):
    return (min(nums), max(nums))

assert g(min_max, [3, -1, 5, 5, 0]) == (-1, 5)
assert g(min_max, [42]) == (42, 42)
assert g(min_max, [-5, -2, -9]) == (-9, -2)
try:
    g(min_max, [])
    assert False
except ValueError:
    print("ValueError")    
assert g(min_max, [1.5, 2, 2.0, -3.1]) == (-3.1, 2)

#2
print("")
print("задача 2")

def unique_sorted(nums):
    return sorted(set(nums))

assert g(unique_sorted, [3, 1, 2, 1, 3]) ==  [1, 2, 3]
assert g(unique_sorted, []) == []             
assert g(unique_sorted, [-1, -1, 0, 2, 2]) == [-1, 0, 2]
assert g(unique_sorted, [1.0, 1, 2.5, 2.5, 0]) == [0, 1.0, 2.5]

#3
print("")
print("задача 3")

def flatten0(mat, b):
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
    b = []
    flatten0(mat, b)
    return b

assert g(flatten, [[1, 2], [3, 4]]) == [1, 2, 3, 4]
assert g(flatten, [[1, 2], (3, 4, 5)]) == [1, 2, 3, 4, 5]
assert g(flatten, [[1], [], [2, 3]]) == [1, 2, 3]
try:
    g(flatten, [[1, 2], "ab"])
    assert False
except TypeError:
    print("TypeError")