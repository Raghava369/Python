n=int(input())
start=int(input())
ans=0
for i in range(n):
    ans=ans^(start+(2*i))
print(ans)
