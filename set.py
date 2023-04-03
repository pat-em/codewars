COLORS = set("RGB")
print(COLORS)
print("________________")


f = "fafafaf"
g = "gagagaga"
h = "hahahah"
k=9
some_row_1 = "".join(f if k>10 else (g+h))
print(some_row_1)
print("________________")
k=11
some_row_1 = "".join(f if k>10 else (g+h))
print(some_row_1)
print("________________")


def triangle(row):
    while len(row)>1:
        row = ''.join( a if a==b else (COLORS-{a,b}).pop() for a,b in zip(row, row[1:]))
    return row


a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)
print(x)

print("/n+++++++++++++++++++++++")
row = "ABCDEFGH"
print("row[1:]",row[1:])
x = zip(row, row[1:])
print(tuple(x))

print("\n+++++++++++++++++++++++")
row_1 = "357421"
y = zip(row_1, row_1[1:])
print(tuple(y))
result = "".join(a if a>b else b for a,b in zip(row_1, row_1[1:]))
print(type(result))
print("RESULT:", result)

print("\n+++++++++++++++++++++++")
myset = set("ABCD")
x = (myset - {"A", "B", "C"}).pop()
y = (myset - {"A", "B", "D"}).pop()
z = (myset - {"A", "C", "D"}).pop()
print("myset:", myset)
print("x, y, z:", ", ".join(x+y+z))