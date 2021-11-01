a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(len(b)):
    if b[i] not in a:
        a.append(b[i])
print(a)
    
