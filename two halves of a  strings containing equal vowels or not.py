s=input()
f=s[:len(s)//2]
e=s[len(s)//2:]
print(f,e)
c=0
count=0
for i in f:
    if i in "aeiouAEIOU":
        c=c+1
for i in e:
    if i in "aeiouAEIOU":
        count=count+1
if count==c:
    print(True)
else:
    print(False)
