l=list(map(int,input().split()))
soe=0
soo=0
for i in range(len(l)):
    if(l[i]%2==0):
        soe+=l[i]
    else:
        soo+=l[i]
print(soe,soo)
