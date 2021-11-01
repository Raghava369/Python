n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i!=1 and i!=n and j!=1 and j!=n):
            print(" ",end=' ')
        else:
            print("*",end=' ')
       
    print(end="\n")
