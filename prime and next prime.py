def primes(n,count):
    if(count==2):
        return
    flag=0
    for i in range(2,n):
        if(n%i==0):
            flag=1
            if(count==0):
                count+=1
            break
    else:
        print(n)
        count+=1
    primes(n+1,count)
    
            
   

n=int(input())
primes(n,0)
