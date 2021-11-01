def primes(n):
    c=1
    l=[]
    l.append(2)
    i=3
    while(c!=n):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            l.append(i)
            c=c+1
        i=i+1
    return l
n=int(input("enter n:"))
print(primes(n))
                
                
        
        
