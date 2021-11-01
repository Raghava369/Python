def prime(a,b):
    flag=0
    for i in range(a,b+1):
        for j in range(2,i):
            if(i%j==0):
                flag=1
        if(flag==0):
            print(i)
        flag=0

a=int(input())
b=int(input())
prime(a,b)
