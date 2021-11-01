n=int(input())
flag=0
for i in range(2,int(n**0.5)):
    if n%i==0:
        flag=1
    else:
        continue
if flag==1:
    print(n,"is not a prime number")
else:
    print(n,"is a prime number")
