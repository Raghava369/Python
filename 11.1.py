exp=input()
l=list(exp)
c=0
i=0
while(i<len(l)-1):
    if c==1:
        c=0
        i+=1
        continue
    if l[i] in "123456789" and l[i+1] not in " 1234567890+=-/)":
        l.insert(i+1,"*")
        c=1
    elif ((l[i]>="a" and l[i]<='z') or (l[i]>="A" and l[i]<='Z')):
        if l[i+1] not in " 1234567890+=-/)":
            l.insert(i+1,"*")
            c=1
    i=i+1
print(l)
exp=""
exp=exp.join(l)
print(exp)
