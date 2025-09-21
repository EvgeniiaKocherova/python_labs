def to_float(s):
    s = s.replace(",", ".")
    return float(s)

num01 = to_float(input("a: "))
num02 = to_float(input("b: "))

total = num01 + num02
average = total/2

print(f"sum={total:.2f}; avg={average:.2f}")


