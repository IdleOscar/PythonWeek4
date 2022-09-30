x = []
n = int(input("Enter the number of row: "))
for i in range(n):
    b = []
    for j in range(n):
        print("Enter the ", i, "row", j, "column: ")
        b.append(int(input()))
    x.append(b)
check = "YES"
for i in range(n):
    for j in range(n):
        if x[i][j] != x[j][i]:
            check = "NO"

print(check)
# 3.2
n = int(input("Enter the number of row: "))
m = int(input("Enter the number of column: "))
x = []
for i in range(n):
    b = []
    for j in range(m):
        print("Enter the ", i, "row", j, "column: ")
        b.append(int(input()))
    x.append(b)
print ("Before: ",x)
max = 0
a = 0
c = 0
for i in range(n):
    for j in range(m):
        if max < x[i][j]:
            max = x[i][j]
            a = i
            c = j

re = x[0][0]
x[0][0] = max
x[a][c] = re
print("After: "x)
