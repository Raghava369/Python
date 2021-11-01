def prime1(n,count):
    if(count==2):
        return
    for i in range(2,n):
        if(n%i==0):
            print(n,"is not prime")
            break
    else:
        print(n,"is prime number")
    prime1(reverse(n),count+1)

def reverse(n):
    a=n
    r=0
    while(n!=0):
        r=r*10+n%10
        n=n//10
    return(r)
    
    
n=int(input())
prime1(n,0)
