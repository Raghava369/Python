def lcm(a,b,greater):
    if(greater%a==0 and greater%b==0):
        return greater
    return lcm(a,b,greater+1)

a=int(input("enter a"))
b=int(input("enter b"))
if a>b:
    greater=a
else:
    greater=b
print(lcm(a,b,greater))
