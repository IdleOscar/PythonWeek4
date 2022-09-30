x = []
n = int(input("Enter the number of row: "))
m = int(input("Enter the number of column: "))
for i in range(n):
    b=[]
    for j in range(m):
        print("Enter the ", i, "row", j, "column: ")
        b.append(int(input()))
    x.append(b)
s = []
for i in range(len(x)):
    s.append(sum(x[i]))
print('large:', x[s.index(max(s))], " = ", max(s))
print('small:', x[s.index(min(s))], " = ", min(s))
#4.2
n = int(input("Enter the number of row: "))
for i in range(n):
    b=[]
    for j in range(n):
        print("Enter the ", i, "row", j, "column: ")
        b.append(int(input()))
    x.append(b)
for i in range(n):
    for j in range(n):
        if x[i][j]>0:
            x[i][j]=1
        else:
            x[i][j]=0
for i in range(n):
    for j in range(n):
        if j<=i:
            print(x[i][j])

