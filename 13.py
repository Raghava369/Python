n=int(input())
l=[]
l.append(1)
l.append(n)
for i in range(2,n//2+1):
    if n%i==0:
        l.append(i)
        l.append(n//i)
l=set(l)
l=list(l)
print(l)
