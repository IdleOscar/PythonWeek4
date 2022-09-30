x = []
n = int(input("Enter the number of row: "))

al = []
def task1 (x,n,al):
    for i in range(n):
        b=[]
        for j in range(n):
            print("Enter the ", i, "row", j, "column: ")
            b.append(int(input()))
        x.append(b)
        al.append(sum(b))

    for i in range(n):
        for j in range(n):
            if i == j:
                x[i][j]/=al[i]
    print (x)
task1 (x,n,al)
def task2(x,n): # I inverted it's like the last element is first and first element is last
    print ("ur array: ",x)
    for i in range(n):

      
        for j in range(n):
            if i == j:
                temp = x[i][j]
                x=[i][j]=x[i][n-j-1]
                x[i][n - j - 1]=temp
    print (x)
task2(x,n)