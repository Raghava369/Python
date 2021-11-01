#python script to find whether a given number is Armstrong number or not:
def noofdigits(n):
    p=0
    temp=n
    while (temp!=0):
        temp=temp//10
        p=p+1
    return p
        
n=int(input("enter a number"))
d=noofdigits(n)
temp=n
ans=0
while (temp!=0):
    r=temp%10
    ans=ans+(r**d)
    temp=temp//10

if(ans==n):
    print("amstrong number")
else:
    print("not a amstrong number")

