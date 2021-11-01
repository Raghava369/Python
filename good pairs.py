names=list(map(int,input().split()))
gp=0
for i in range(len(names)):
    for j in range(i+1,len(names)):
        if(names[i]==names[j]):
            gp+=1
print(gp)
        
