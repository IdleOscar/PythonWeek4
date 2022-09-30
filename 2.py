x=[]
n = int(input("Enter the number of row: "))
for i in range(n):
    b=[]
    for j in range(n):
        print("Enter the ", i, "row", j, "column: ")
        b.append(int(input()))
    x.append(b)
def magic(x):
    for i in range(n):
        row = 0
        column = 0
        for j in range(n):
            row  += x[i][j]
            column += x[j][i]
        if not (row == column):
            return False

    return True

if magic(x) == True:
    print("Magic Square")
else:
    print("Not a magic Square")
#2.2
