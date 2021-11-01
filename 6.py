n=input()
s=input()
l=[]
r=0
c=0
for i in range(len(n)):
    if(n[i]==" " ):
        l.append(n[r:i])
        c=c+1
        r=i+1
    if(i==len(n)-1):
        l.append(n[r:i+1])
        c=c+1
    if len(l)!=0 and l[c-1]==s  :
        l[c-1]=l[c-1][::-1]
n=" ".join(l)
        
        
print(n)
    
    


