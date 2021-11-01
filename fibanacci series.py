def fiba(n):
    
    if n==1:
        return 0
    if n==2:
        return 1
    
    return print(fiba(n-1)+fiba(n-2))

    
n=int(input("enter a number"))
print(fiba(n))


    
