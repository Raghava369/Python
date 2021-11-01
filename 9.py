#python script to find whether a given number is perfect or not

def perfectn():
    n=int(input("enter a number"))
    res=0
    print("the factors of a given number:")
    for i in range(1,n):
        if(n%i==0):
            print(i,end=' ')
            res=res + i
    if(res==n):
        print("perfect number")
    else:
        print('not perfect number')
              
