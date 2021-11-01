import random
l=[]
sum=0
en=[]
for i in range(20):
    r=random.randint(1,100)
    l.append(r)
    sum=sum+r
    if r%2==0:
        en.append(r)
print(l)
print(sum/20)
l.sort()
print("largest",l[len(l)-1])
print("smallest",l[0])
print("second largest",l[len(l)-2])
print("second smallest",l[1])
print("even numbers",en)


