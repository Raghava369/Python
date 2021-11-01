import random
l=[]
for i in range(100):
    l.append(random.randint(0,1))
print(l)
c=0
maximum=0
for i in range(len(l)):
    if l[i]==1:
        if c>maximum:
            maximum=c
        c=0
        
    if l[i]==0:
        c=c+1
print(maximum)
