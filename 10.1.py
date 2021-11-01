n=int(input("enter a integer"))
l=[]
n=str(n)
c=0
p=0
for i in range(len(n)):
    l.append(n[i])
l=l[::-1]
for i in range(0,len(l)):
    c=c+1
    if c==3 and p==0:
        l.insert(i+1,",")
        p=1
        c=0
    if p==1 and c==4:
        l.insert(i+1,",")
        c=0
l=l[::-1]
n=""
n=n.join(l)
print(n)


    
