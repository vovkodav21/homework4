a = [12, 345, 98, 5, 9, 111]
b = [111, 55, 43, 98, 12]
c = []
for value in b:
    if value not in a:
        c.append(value)
print(c)
