x = []
n = int(input("Enter the number of row: "))
for i in range(n):
    b=[]
    for j in range(n):
        print("Enter the ", i, "row", j, "column: ")
        b.append(int(input()))
    x.append(b)
def task1(x,n):
    k = int(input("Inputr the value u gonna over: "))
    al=[]
    for i in range(n):
        for j in range(n):
            if x[i][j]%k==0:
                al.append(x[i][j])
    print(al)
    print(max(al))
task1(x,n)