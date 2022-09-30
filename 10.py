x = []
n = int(input("Enter the number of row: "))
m = int(input("Enter the number of column: "))
al=[]
for i in range(n):
    b=[]
    for j in range(m):
        print("Enter the ", i, "row", j, "column: ")
        b.append(int(input()))
    b.sort()
    x.append(b)
    al(max(b))
print(x)
print(al)