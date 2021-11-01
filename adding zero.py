def czero(l):
    k=len(l)
    for i in range(len(l)-2,-1,-1):
        if(l[i]==0):
            l.insert(i+1,0)
    if(len(l)-k)==0:
        print(l)
    else:
        print(l[:-(len(l)-k)])
        
        
l=list(map(int,input().split()))
print(czero(l))
