n=input()
p=int(input())
s=""
for i in range(1,len(n),2):
    s=s+ (n[i-1]*int(n[i]))
print(s)
try:
    print(s[p-1])
except:
    print(-1)
    
    


