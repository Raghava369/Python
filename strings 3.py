n=input()
s=input()
l=[]
r=0
for i in range(len(n)):
    if(n[i]==" " ):
        l.append(n[r:i])
        r=i+1
    if(i==len(n)-1):
        l.append(n[r:i+1])
for i in  range(len(l)):
    if l[i]==s:
        l[i]=l[i][::-1]
n=" ".join(l)
        
        
print(n)
    
    


