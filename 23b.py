def sortedlist(L1,L2):
    l1=len(L1)
    l2=len(L2)
    r=[]
    tl=l1+l2
    i=0
    j=0
    for k in range(tl):
        if(i==l1 and j!=l2):
            r.append(L2[j])
            j=j+1
            continue
        if(j==l2 and i!=l1):
            r.append(L1[i])
            i=i+1
            continue
        if(i!=l1 and L1[i]<=L2[j]):
            r.append(L1[i])
            i=i+1
        elif(j!=l2 and L1[i]>L2[j]):
            r.append(L2[j])
            j=j+1
      
    return r
L1=list(map(int,input().split()))
L2=list(map(int,input().split()))
print(sortedlist(L1,L2))

             
    
