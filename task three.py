A = int(input("Введіть число А: "))
B = int(input("Введіть число В: "))
if A<B:
    for i in range(A, B+1):
        print(i)
else:
    for i in range(A, B-1, -1):
        print(i)