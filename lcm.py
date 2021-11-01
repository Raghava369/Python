a=int(input())
b=int(input())
if a>b:
    greater=a
else:
    greater=b
while greater%a!=0 or greater%b!=0:
        greater+=1
print(greater)
