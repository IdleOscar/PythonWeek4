x = []
n = int(input("Enter the number of row: "))
small=[]
for i in range(n):
    b=[]
    for j in range(n):
        print("Enter the ", i, "row", j, "column: ")
        b.append(int(input()))
    x.append(b)
    small.append(min(b))
print("Ur array: ",x)
print("The small numbers: ",small)
for i in range(n):
    min=x[0][i]
    for j in range(n):
        if min>x[j][i]:
            min = x[j][i]
    print(min)
#6.2