x = []
n = int(input("Enter the number of row: "))
m = int(input("Enter the number of column: "))
for i in range(n):
    b=[]
    for j in range(m):
        print("Enter the ", i, "row", j, "column: ")
        b.append(int(input()))
    x.append(b)

for i in range(n):
    x[i].sort()
print(x)
#5.2
x = []
n = int(input("Enter the number of row: "))
m = int(input("Enter the number of column: "))
for i in range(n):
    b=[]
    for j in range(m):
        print("Enter the ", i, "row", j, "column: ")
        b.append(int(input()))
    x.append(min(b))

print("Minimals of rows: ",x)
for i in range(n):
    if x[i]%2!=0:
        x[i]=1
    else:
        x[i] = 0
print("The task: ",x)

