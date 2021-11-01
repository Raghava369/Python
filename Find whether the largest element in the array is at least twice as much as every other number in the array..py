l=list(map(int,input().split()))
m=max(l)
c=0
for i in l:
    if(i!=m):
        if(i*2<=m):
            c+=1
    elif(i==m):
        result=l.index(i)
if(c==len(l)-1):
    print(result)
else:
    print(-1)
    
        

