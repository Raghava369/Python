def no_of_factors(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c=c+1
    return c+2
n=int(input())
print(no_of_factors(n))

