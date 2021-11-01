import math
def prime(n):
    for i in range(2,int(math.sqrt(n))):
        if n%i ==0:
            return False
    else:
        return True
def mp(n):
    if(prime(n)):
        while n:
            if prime(n%10)==False:
                return False
            n=n//10
        else:
            return True
    else:
        return False

n=int(input("enter a number"))
if mp(n):
    print("mega prime")
else:
    print("not a mega prime")
