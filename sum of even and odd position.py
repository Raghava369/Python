l=list(map(int,input().split()))
soep=0
soop=0
for i in range(len(l)):
    if(i%2==0):
        soep+=l[i]
    else:
        soop+=l[i]
print(soep,soop)
