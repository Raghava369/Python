s=int(input("enter staring point"))
e=int(input("enter ending point"))
n=int(input("enter number"))
for i in range(s,e+1):
    if(i%n==0):
        print(i,end=" ")
    else:
        continue
