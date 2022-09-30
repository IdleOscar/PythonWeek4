n = int(input("Enter the number of row: "))
m = int(input("Enter the number of column: "))
b = []
for i in range(n):
    x = []
    for j in range(m):
        print("Enter the ", i, "row", j, "column: ")
        x.append(int(input()))
    b.append(x)
sum = 0
for i in range(n):
    for j in range(m):
        if i == j and b[i][j] > 0:

            sum += b[i][j]
print("The sum is: ", sum)
#1.2
n = int(input("Enter the number of row: "))
m = int(input("Enter the number of column: "))
b = []
for i in range(n):
    x=[]
    for j in range(m):
        print("Enter the ", i, "row", j, "column: ")
        x.append(int(input()))
    b.append(x)
max = 0
min = 0
for i in range(n):
    for j in range(m):
        if max < b[i][j]:
            max = x[i][j]
        if min > b[i][j]:
            min = x[i][j]
    print("The max of ", i, "row is : ", max)
    print("The min of ", i, "row is : ", min)


