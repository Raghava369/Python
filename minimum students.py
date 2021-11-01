l=list(map(int,input().split()))
h=sorted(l)
c=0
for i in range(len(l)):
    if(h[i]!=l[i]):
        c+=1

print(c)
