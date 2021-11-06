l=list(map(int,input().split()))
c=1
r=[]
for i in range(len(l)):
    for j in range(i,len(l)):
        r.append(l[i:j+1])
print(r)
t=[]  

for i in range(len(r)):
    flag=0
    for j in  range(len(r[i])):#3 3 1
        for k in range(len(r[i])):
            if abs(r[i][j]-r[i][k])>1:
                flag=1
                break
        if flag==1:
                break
    else:
        t.append(len([i]))
print(max(t))


        
            
    

    
    
