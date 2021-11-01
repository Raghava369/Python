l=list(map(int,input().split()))
ec=int(input())
m=max(l)
for i in range(len(l)):
    if l[i]+ec >= m :
        l[i]="True"
    else:
        l[i]="False"
print(l)
