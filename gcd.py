a=int(input())
b=int(input())
while(b!=0):
    rem=a%b
    a=b
    b=rem
print(a)
