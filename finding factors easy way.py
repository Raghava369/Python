n=int(input())
l=[]
l.extend([1,n])
for i in range(2,n//2):
    if n%i==0:
        l.extend([i,n//i])
l=set(l)
l=list(l)
print(sorted(l))
        
