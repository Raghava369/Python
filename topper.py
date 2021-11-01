a={}
m=0
n=int(input("enter number of students:"))
for i in range(n):
    x=input("enter student name")
    y=list(map(int,input().split()))
    a[x]=y
    average=sum(y)/len(y)
    if(m<average):
        m=average
        topper=x
print(topper)
    
