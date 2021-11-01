
n=input()
c=1
l=[]
for i in range(len(n)-1):
    if ord(n[i])+1==ord(n[i+1]):
        c=c+1
    else:
        l.append(c)
        c=1
        continue
if ord(n[len(n)-2])+1==ord(n[len(n)-1]):
    l.append(c) 
print(max(l))
    
