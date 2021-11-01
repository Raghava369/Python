l=list(map(int,input().split()))
max=l[0]
for i in range(1,len(l)):
    if(l[i]>max):
        max=l[i]
    else:
        continue
print(max)
