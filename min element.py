l=list(map(int,input().split()))
min=l[0]
for i in range(1,len(l)):
    if(l[i]<min):
        min=l[i]
    else:
        continue
print(min)
